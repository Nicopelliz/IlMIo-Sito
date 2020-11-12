from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms


class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-line'}))
    first_name = forms.CharField (max_length=100, widget=forms.TextInput(attrs={'class': 'form-line'}))
    last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-line'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-line'}))
    password1 = forms.CharField(max_length=100, label= 'Password', widget=forms.TextInput(attrs={'class': 'form-line'}))
    password2 = forms.CharField(max_length=100, label= 'Password confirmation', widget=forms.TextInput(attrs={'class': 'form-line'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-line'}))
    first_name = forms.CharField (max_length=100, widget=forms.TextInput(attrs={'class': 'form-line'}))
    last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-line'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-line'}))
    # last_login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-line'}))
    # is_superuser = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    # is_staff = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    # is_active = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    # date_joined = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-line'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password') # 'last_login',
            # 'is_superuser', 'is_staff', 'is_active', 'date_joined')
