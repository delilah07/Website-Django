from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Destiny Franks',
        'title': "Blog post 1",
        'content': 'This is my first blog post',
        'date_posted': '7th August, 2021'
    },
    {
        'author': 'Jane Doe',
        'title': "Blog post 2",
        'content': 'This is my first new blog post',
        'date_posted': '14th August, 2021'
    }
]

# Create your views here.
def home(request):
    # return HttpResponse(
    #     "<h1>Blog Home</h1>"
    #     "<hr>"
    #     "<button>Send</button>"
    # )
    context = {
        'posts': posts
    }
    return render(request, 'index.html', context)

def about(request):
    # return HttpResponse("<h1>About Blog</h1>")
    return render(request, 'about.html', {'title': "About my blog"})