from .models import Comment, Post
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'content', 'prefazione')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control  form-title'}),
            'content': forms.Textarea(attrs={'class': 'form-control  form-content'}),
            'author': forms.TextInput(attrs={'class': 'form-control  form-author', 'id': 'author-user', 'value': '', 'type': 'hidden'}),
            'prefazione': forms.Textarea(attrs={'class': 'form-control  form-prefazione'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'prefazione')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control  form-title'}),
            'content': forms.Textarea(attrs={'class': 'form-control  form-content'}),
            'prefazione': forms.Textarea(attrs={'class': 'form-control  form-prefazione'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-comment'}),
            'email': forms.EmailInput(attrs={'class': 'form-comment'}),
            'body': forms.Textarea(attrs={'class': 'form-comment-area'}),
        }
