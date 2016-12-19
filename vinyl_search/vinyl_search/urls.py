
from django.conf.urls import url
from django.contrib import admin
from search_app import views
from accounts.views import register, login
from django.contrib.auth.views import logout
from django.conf import settings
from django.conf.urls.static import static

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

    # rest api
    url(r'^api/queries/$', views.search_app_list),
    url(r'^api/queries/(?P<pk>[0-9]+)/$', views.query_detail),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
