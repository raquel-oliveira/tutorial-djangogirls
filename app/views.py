from django.shortcuts import render
from .models import Post
from django.utils import timezone


# Create your views here.

def post_list(request):
    posts = Post.objects.order_by('published_date')
    return render(request, 'app/post_list.html', {'posts': posts})
