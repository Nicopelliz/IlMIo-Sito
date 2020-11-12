from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import PostForm, EditForm, CommentForm
from .models import Post, Comment
from django.urls import reverse_lazy


class PostList(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog_page.html'


# class PostDetail(DetailView):
#     model = Post
#     template_name = 'post_details.html'

def post_detail(request, pk):
    template_name = 'post_details.html'
    post = get_object_or_404(Post, id=pk)
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
# fields = '__all__'


# class AddComment(CreateView):
#  model = Comment
#   form_class = CommentForm
#   template_name = 'post_details.html'


class UpdatePost(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
# fields = {'content', 'title'}


class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('blog_home')





