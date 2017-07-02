# coding=utf-8

from blog.models import BlogsPost
from django.shortcuts import render_to_response


# Create your views here.
def index(request):
    blog_list = BlogsPost.objects.all()
    return render_to_response('index.html', {'blogs': blog_list})


