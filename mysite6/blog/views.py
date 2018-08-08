from django.shortcuts import render
from .models import BlogArticle
# Create your views here.

def blog_title(request):
    blogs = BlogArticle.objects.all()
    return render(request,'blog/titles.html',{'blogs':blogs})

def blog_article(request,article_id):
    article = BlogArticle.objects.get(id=article_id)
    return render(request,'blog/content.html',{'article':article})

def login(request):
    pass