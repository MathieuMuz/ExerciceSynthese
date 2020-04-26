from django import forms


class ResearchForm(forms.Form):
    album = forms.CharField(max_length=100)
