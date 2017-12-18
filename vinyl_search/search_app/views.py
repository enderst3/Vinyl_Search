import selenium
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from search_app.models import VinylQuery
from .forms import VinylQueryForm
from .models import VinylQuery
from private.secrets import client_id, client_secret, discogs_key
from imgurpython import ImgurClient
from django.contrib.auth.decorators import login_required
from search_app.forms import ContactForm
from django.core.mail import EmailMessage 
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template
import requests
import discogs_client
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from search_app.models import VinylQuery
from search_app.serializers import VinylQuerySerializer
from django.views.decorators.csrf import csrf_exempt


@login_required
def app(request):
    '''
    search code
    '''
    album = None
    client = ImgurClient(client_id, client_secret)
    '''
    upload and save image to database
    '''
    if request.method == 'POST':
        upload = request.FILES['file']
        vq = VinylQuery.objects.create(user=request.user, query_image=upload)
        vq.save()
        image = client.upload_from_path(vq.query_image.path, anon=False)
        vq.imgur_url = image.get('link', None)
        vq.save()


        '''
        need to search this base url
        https://www.google.com/searchbyimage?&image_url=vq.imgur_url

        Then open and google search 

        '''
        # selenium web driver, opens firefox
        driver = webdriver.Firefox()
        # goes to google
        driver.get('https://www.google.com/searchbyimage?&image_url='+vq.imgur_url)
        # finds the input field
        #image_url_field = driver.find_element_by_name('q')
        # populates the image url
        #image_url_field.send_keys(vq.imgur_url)
        # clicks submit
        #image_url_field.submit()
        # waits 2 seconds
        #time.sleep(5)
        # finds search by image link, then clicks
        #driver.find_element_by_xpath("//a[contains(., 'searchby')]").click()
        # waits 5 seconds
        #time.sleep(1)
        # finds the best guess and copies the info
        best_guess = driver.find_element_by_class_name('_gUb').text
        # discogs keys and api call
        d = discogs_client.Client('vinyl_search/0.1', user_token=discogs_key)
        # getting the results
        results = d.search(best_guess)
        sm_results = list()
        # finds the first 5 results
        for index, result in enumerate(results):

            if index >= 5:
                break

            thumb_link = result.data
            sm_results.append(thumb_link)

        r = sm_results[0]
        vq.result_title = r['title']
        vq.result_format = r['thumb']
        vq.result_url = r['uri']
        vq.save()

    elif request.method == 'GET':
        form = VinylQueryForm()
        sm_results = list()
    # import ipdb; ipdb.set_trace()
    context = {'results': sm_results}

    return render(request, 'capstone.html', context)


def user_history(request):
    '''
    user history
    '''
    vq = VinylQuery.objects.filter(user=request.user)
    context = {'results': vq}
    return render(request, 'user_history.html', context)


def contact(request):
    '''
    contact and email info
    '''
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')
            template = get_template('contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content})
            content = template.render(context)

            email = EmailMessage("New contact form submission",
                content, "Vinyl Search" + '', ['enderst3@gmail.com'],
                headers={'Reply-To': contact_email})

            email.send()
            return redirect('contact')

    return render(request, 'contact.html', {'form': form_class})


class JSONResponse(HttpResponse):
    """
    rest framework
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def search_app_list(request):
    """
    List data
    """
    if request.method == 'GET':
        vqs = VinylQuery.objects.all()
        serializer = VinylQuerySerializer(vqs, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = VinylQuerySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def query_detail(request, pk):
    """
    Retrieve query data
    """
    try:
        query = VinylQuery.objects.get(pk=pk)
    except VinylQuery.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = VinylQuerySerializer(query)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = VinylQuerySerializer(query, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        query.delete()
        return HttpResponse(status=204)
