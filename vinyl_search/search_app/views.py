from django.shortcuts import render
from django.http import HttpResponseRedirect
from search_app.models import VinylQuery
from .forms import VinylQueryForm
from .models import VinylQuery
from private.secrets import client_id, client_secret
from imgurpython import ImgurClient


album = None
client = ImgurClient(client_id, client_secret)

def capstone(request):
    return render(request, "capstone.html")


def upload_image(request):

    if request.method == 'POST':
        form = VinylQuery()
        form.query_image = request.FILES['file']
        form.save()
        #import pdb; pdb.set_trace()
        image = client.upload_from_path(form.query_image.path, anon=False)
        import pdb; pdb.set_trace()

    else:
        form = VinylQueryForm()

    return HttpResponseRedirect("/")
