from django.urls import path
from .views import home, music, coding, crypto, organic, projects


urlpatterns = [
    path('', home, name='home'),
    # path('about/', bio, name='bio'),
    path('music/', music, name='music'),
    path('coding/', coding, name='coding'),
    path('organic/', organic, name='organic'),
    path('projects/', projects, name='projects'),
    # path('crypto-blog/', crypto, name='crypto'),
]
