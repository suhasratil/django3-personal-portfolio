from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def all_blogs(requests):
    blogs=Blog.objects.order_by('-date')
    return render(requests, 'blog/all_blogs.html', {'blogs' : blogs})

def details(hello, blog_id):
    blog=get_object_or_404(Blog, pk=blog_id)
    return render(hello, 'blog/details.html', {'blog':blog})