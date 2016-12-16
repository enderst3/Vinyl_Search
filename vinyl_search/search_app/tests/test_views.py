from django.test import RequestFactory
from .. import views
import pytest
from mixer.backend.django import mixer
from django.contrib.auth.models import AnonymousUser
pytestmark = pytest.mark.django_db


class TestView:
    
    def app(self):
        req = RequestFactory().get('/')
        resp = views.app.as_view()(req)
        assert resp.status_code == 200, 'Should be callable'
        
        
    def test_anonymous(self):
        req = RequestFactory().get('/')
        req.user = AnonymousUser()
        resp = views.app.as_view()(req)
        assert 'login' in resp.url,'Should redirect to login'
        
        
    def test_superuser(self):
        user = mixer.blend('auth.User', is_superuser=True)
        req = RequestFactory().get('/')
        req.user = user
        resp = views.app.as_view()(req)
        assert resp.status_code == 200, 'Should be callable by superuser'
        
