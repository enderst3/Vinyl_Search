from django.shortcuts import render
from django.http import HttpResponseRedirect
from search_app.models import VinylQuery
from .forms import VinylQueryForm
from .models import VinylQuery
from private.secrets import client_id, client_secret
from imgurpython import ImgurClient
from django.contrib.auth.decorators import login_required


@login_required
def app(request):

    album = None
    client = ImgurClient(client_id, client_secret)

    if request.method == 'POST':
        upload = request.FILES['file']
        # import pdb; pdb.set_trace()
        vq = VinylQuery.objects.create(user=request.user, query_image=upload)
        vq.save()
        image = client.upload_from_path(vq.query_image.path, anon=False)
        vq.imgur_url = image.get('link', None)
        vq.save()
        # import pdb; pdb.set_trace()

    elif request.method == 'GET':
        form = VinylQueryForm()

    context = {}

    return render(request, 'capstone.html', context)
