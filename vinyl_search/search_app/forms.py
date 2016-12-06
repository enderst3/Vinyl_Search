from django import forms
from .models import VinylQuery
from django import forms


class VinylQueryForm(forms.ModelForm):

    class Meta:
        model = VinylQuery
        fields = ('query_image', 'imgur_url')

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )