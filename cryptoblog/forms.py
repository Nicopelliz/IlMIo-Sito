from .models import Comment, Post
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'content')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control  form-title'}),
            'content': forms.Textarea(attrs={'class': 'form-control  form-content'}),
            'author': forms.Select(attrs={'class': 'form-control  form-author'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control  form-title'}),
            'content': forms.Textarea(attrs={'class': 'form-control  form-content'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
