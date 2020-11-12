from django.urls import path
from .views import UserRegister, UserEditProfile, password_changed
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', UserRegister.as_view(), name='register'),
    path('edit_profile/', UserEditProfile.as_view(), name='edit_profile'),
    path('password/', auth_views.PasswordChangeView.as_view(template_name = 'registration/change_password.html', success_url = 'password_changed'), name='password_change'),
    path('password/password_changed/', password_changed, name = 'password_changed')
]
