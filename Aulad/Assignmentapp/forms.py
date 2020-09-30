from django import forms
from .models import *

class ProducerForm(forms.ModelForm):
    class Meta:
        model = Producer
        fields = ['name','city','state','country']
class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        exclude = []
class SongForm(forms.ModelForm):
    class Meta:
        model=Song
        exclude = []
