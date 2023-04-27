from django.shortcuts import render
from django.views.generic import ListView, DetailView
from sun.models import Post

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
