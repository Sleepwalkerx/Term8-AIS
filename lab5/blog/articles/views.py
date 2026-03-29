from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ArticleForm
from .models import Article


def archive(request):
    posts = Article.objects.all()
    return render(request, "articles/archive.html", {"posts": posts})

def get_article(request, article_id):
    post = get_object_or_404(Article, id=article_id)
    return render(request, "articles/article.html", {"post": post})

def create_post(request):
    if not request.user.is_authenticated:
        raise Http404

    if request.method == "POST":
        form = ArticleForm(request.POST)

        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect("get_article", article_id=article.id)
    else:
        form = ArticleForm()

    return render(request, "articles/create_post.html", {"form": form})