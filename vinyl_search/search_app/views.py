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
import requests
import discogs_client

@login_required
def app(request):

    album = None
    client = ImgurClient(client_id, client_secret)

    if request.method == 'POST':
        upload = request.FILES['file']
        vq = VinylQuery.objects.create(user=request.user, query_image=upload)
        vq.save()
        image = client.upload_from_path(vq.query_image.path, anon=False)
        vq.imgur_url = image.get('link', None)
        vq.save()
        browser = webdriver.Firefox()
        browser.get('https://images.google.com/')
        image_url_field = browser.find_element_by_name('q')
        image_url_field.send_keys(vq.imgur_url)
        image_url_field.submit()
        time.sleep(1)
        browser.find_element_by_xpath("//a[contains(., 'search by')]").click()
        time.sleep(4)
        best_guess = browser.find_element_by_class_name('_gUb').text
        #print(best_guess)
#        import ipdb; ipdb.set_trace()
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


