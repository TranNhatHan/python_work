from django import forms

from .models import Page, Post

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['name']
        labels = {'text': ''}

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
