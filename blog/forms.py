from django import forms
from ckeditor.fields import RichTextField

class PostsForm(forms.Form):

    title = forms.CharField(max_length=40)
    subtitle = forms.CharField(max_length=40)
    body = RichTextField(max_length=1000)
    author = forms.CharField(max_length=40)
    date = forms.DateField()
    image = forms.ImageField()