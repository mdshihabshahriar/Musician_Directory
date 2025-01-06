from django import forms
from .models import Musician, Album

class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = '__all__'

class AlbumForm(forms.ModelForm):
    release_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )

    class Meta:
        model = Album
        fields = '__all__'