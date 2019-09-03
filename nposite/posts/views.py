from django.shortcuts import render
from django.views.generic import DetailView, CreateView, DeleteView, ListView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy


# Create your views here.
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('posts:created')


def created(request):
    return render(request, 'posts/created.html')


class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list'
