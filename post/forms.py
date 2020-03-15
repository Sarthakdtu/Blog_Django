from django import forms
from trix.widgets import TrixEditor

class PostForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField(widget=TrixEditor)
    