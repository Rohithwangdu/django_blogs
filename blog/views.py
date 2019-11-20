from django.shortcuts import render
from .models import Post


def home(request):
    '''A sample home page'''
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    '''A sample about page'''
    return render(request, 'blog/about.html', {'title': 'About'})
