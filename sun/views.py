from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Post
from .utils import fetch_data_from_api
from django.http import JsonResponse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


class PostListView(ListView):
    model = Post
    template_name = 'sun/post_list.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class PostDetailView(DetailView):
    model = Post
    template_name = 'sun/post_detail.html'

def about(request):
    return render(request, 'sun/about.html', {'title': 'About'})

def frontpage(request):
    return render(request, 'sun/frontpage.html')

def api_data_view(request):
    data = fetch_data_from_api()
    if data:
        return JsonResponse(data)
    else:
        return JsonResponse({"error": "Failed to fetch data from the API"}, status=500)
    
def posts_list(request):
    posts = Post.objects.all().order_by('date_posted')  # Fetch all posts and order them by date
    return render(request, 'sun/posts_list.html', {'posts': posts})



@login_required
def add_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        date_posted = timezone.now()

        # Get the logged-in user's information
        author = request.user

        new_post = Post(title=title, content=content, date_posted=date_posted, author=author)
        new_post.save()

        return redirect('posts_list')
    else:
        return render(request, 'sun/add_post.html')
    
def about_me(request):
    return render(request, 'sun/about_me.html')

