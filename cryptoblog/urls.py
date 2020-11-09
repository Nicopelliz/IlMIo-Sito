from .views import PostList, PostDetail, AddPost, UpdatePost, DeletePost
from django.urls import path

urlpatterns = [
    path('', PostList.as_view(), name='blog_home'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('add-post/', AddPost.as_view(), name='add_post'),
    path('edit-post/<int:pk>', UpdatePost.as_view(), name='update_post'),
    path('post/<int:pk>/delete/', DeletePost.as_view(), name='delete_post'),
]
