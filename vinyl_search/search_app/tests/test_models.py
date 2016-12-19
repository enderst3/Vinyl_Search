import pytest
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db


class TestQuery:

    def test_model(self):
        obj = mixer.blend('search_app.VinylQuery')
        assert obj.pk == 1, 'Should create a query'
