from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'about', 'text', 'author', 'category', 'image')


class PostForm2(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'about', 'text', 'category', 'author')
