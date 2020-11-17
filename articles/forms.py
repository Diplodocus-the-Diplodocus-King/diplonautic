from django import forms
from . import models

class CreateArticle(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'body', 'slug', 'image']

class CreateComment(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['title', 'body']