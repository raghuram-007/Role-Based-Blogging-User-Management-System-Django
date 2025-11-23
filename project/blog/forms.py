from django import forms
from .models import Post
from django import forms
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'category', 'summary', 'content', 'status']


