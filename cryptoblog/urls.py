from .views import PostList, post_detail
from django.urls import path

urlpatterns = [
    path('', PostList.as_view(), name='blog_home'),
    path('<slug:slug>/', post_detail, name='post_detail')
]