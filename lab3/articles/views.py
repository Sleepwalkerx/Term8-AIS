from django.shortcuts import render
from .models import Article

def archive(request):
    posts = Article.objects.all()
    return render(request, "articles/archive.html", {"posts": posts})