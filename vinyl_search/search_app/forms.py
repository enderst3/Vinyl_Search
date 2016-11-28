from django import forms
from .models import VinylQuery

class VinylQueryForm(forms.ModelForm):

    class Meta:
        model = VinylQuery
        fields = ('query_image', )
