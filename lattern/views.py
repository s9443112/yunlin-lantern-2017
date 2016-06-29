from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Post, Photo
# Create your views here.
def index(request):
    return render(request, 'index.html',{
        'current_time':datetime.now(),
    })

def home(request):
    post_list = Post.objects.all()
    return render(request,'home.html',{
        'post_list':post_list,
        'current_time':datetime.now(),
    })

def billboard(request):
    post_list = Post.objects.order_by('-created_at')
    return render(request,'billboard.html',{
        'post_list':post_list,
        'current_time':datetime.now(),
    })

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request,'post.html',{'post':post})

def about(request):
    return render(request,'about.html')

def picture(request):
    picture_list = Photo.objects.order_by('-created_at')
    return render(request,'picture.html',{
        'picture_list':picture_list,
        'current_time':datetime.now(),
    })
