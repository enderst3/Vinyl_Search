import selenium
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.shortcuts import render
from django.http import HttpResponseRedirect
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


# search code
@login_required
def app(request):
    album = None
    client = ImgurClient(client_id, client_secret)
    # upload and save image to database
    if request.method == 'POST':
        upload = request.FILES['file']
        vq = VinylQuery.objects.create(user=request.user, query_image=upload)
        vq.save()
        image = client.upload_from_path(vq.query_image.path, anon=False)
        vq.imgur_url = image.get('link', None)
        vq.save()
        
        # selenium web driver
        driver = webdriver.Firefox()
        driver.get('https://images.google.com/')
        image_url_field = driver.find_element_by_name('q')
        image_url_field.send_keys(vq.imgur_url)
        image_url_field.submit()
        time.sleep(1)
        driver.find_element_by_xpath("//a[contains(., 'search by')]").click()
        time.sleep(4)
        best_guess = driver.find_element_by_class_name('_gUb').text
        d = discogs_client.Client('vinyl_search/0.1', user_token=discogs_key)
        results = d.search(best_guess)
        sm_results = list()

        for index, result in enumerate(results):

            if index >= 5:
                break

            thumb_link = result.data
            sm_results.append(thumb_link)

    elif request.method == 'GET':
        form = VinylQueryForm()
        sm_results = list()

    context = {'results': sm_results}

    return render(request, 'capstone.html', context)


# contact and email info
def contact(request):
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
                content,"Vinyl Search" +'',['enderst3@gmail.com'],
                headers = {'Reply-To': contact_email})
            
            email.send()
            return redirect('contact')

    return render(request, 'contact.html', {'form': form_class})

