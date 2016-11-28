from django.shortcuts import render
from django.http import HttpResponseRedirect
from search_app.models import VinylQuery
from django.template import RequestContext as ctx
from .forms import VinylQueryForm
from .models import VinylQuery
# Create your views here.
def capstone(request):
    return render(request, "capstone.html")


def upload_image(request):

    if request.method == 'POST':
        #form = VinylQueryForm(request.POST, request.FILES)
        form = VinylQuery()
        form.query_image = request.FILES['file']
        form.save()

        #if form.is_valid():
            #image = form.save()

    else:
        form = VinylQueryForm()
    return HttpResponseRedirect("/")
    #return render('query_upload.html', locals(), ctx(request))
