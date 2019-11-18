from django.shortcuts import render


posts =[
    {
        'author': 'Iron man',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted':'Nov 18, 2019'
    },
    {
        'author': 'Capt Marvel',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted':'Nov 19, 2019'
    }
]
def home(request):
    '''A sample home page'''
    context = {
        'posts':posts
    }
    return render(request, 'blog/home.html',context)


def about(request):
    '''A sample about page'''
    return render(request, 'blog/about.html',{'title':'About'})
