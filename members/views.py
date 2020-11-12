from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import RegisterForm, EditProfileForm
from django.shortcuts import render


class UserRegister(CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserEditProfile(UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('blog_home')

    def get_object(self):
        return self.request.user


def password_changed(request):
    return render(request, 'registration/password_changed.html', {})
