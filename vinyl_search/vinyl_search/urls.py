
from django.conf.urls import url
from django.contrib import admin
from search_app import views
from accounts.views import register, login
from django.contrib.auth.views import logout

# django admin
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.app, name='app'),
    url(r'^user_history/', views.user_history),
    
    # contact page
    url(r'^contact/$', views.contact, name='contact'),
    
    # user auth urls
    url(r'^accounts/register/$', register),
    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', logout, {'next_page': '/'}),
    
]
