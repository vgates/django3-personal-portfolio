from django.shortcuts import render, get_object_or_404
from .models import Blog


def all_blogs(request):
    # desc order of date - only first 5
    blogs = Blog.objects.order_by('-date')[:5]
    return render(request, 'blog/all_blog.html', {'blogs': blogs})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})
