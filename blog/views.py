from django.shortcuts import render
from .models import Post
# Create your views here.


def home_view(request):
    post_list = Post.objects.all().order_by('-published_date')
    context = {
        'posts': post_list,
    }
    return render(request, 'blog/home.html', context)


def contact_view(request):
    return render(request, 'blog/contact.html')


def Detail_view(request, slug):
    post = Post.objects.get(slug=slug)
    context = {
        'post': post
    }   
    return render(request, 'blog/PostDetails.html', context)
