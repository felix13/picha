from django import forms

from picha.models import Picture


class PictureForm(forms.ModelForm):
    name = forms.CharField(
       widget=forms.TextInput(attrs={'class': 'form-control'}),
       max_length=50)

    class Meta:
        model = Picture
        fields = ['name', 'image']
