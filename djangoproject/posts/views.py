from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.
def index(request):
    posts = Post.objects.all()[:10]
    context = {
         'title': 'Latest Posts',
         'post': posts
    }
    return render(request,'posts/index.html',context)

def details(request, id):
    post = Post.objects.get(id = id)
    context = {
        'post': post
    }
    return render(request,'posts/details.html',context)

    #return HttpResponse('Hello from Posts')
   # return render(request, 'posts/index.html')