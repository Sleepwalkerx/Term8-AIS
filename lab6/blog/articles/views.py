from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ArticleForm, LoginUserForm, RegisterUserForm
from .models import Article


def archive(request):
    posts = Article.objects.all().order_by("-created_date", "-id")
    return render(request, "articles/archive.html", {"posts": posts})


def get_article(request, article_id):
    post = get_object_or_404(Article, id=article_id)
    return render(request, "articles/article.html", {"post": post})

@login_required(login_url="login")
def create_post(request):
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


def register_user(request):
    if request.user.is_authenticated:
        return redirect("archive")

    if request.method == "POST":
        form = RegisterUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("archive")
    else:
        form = RegisterUserForm()

    return render(request, "articles/register.html", {"form": form})


def login_user(request):
    if request.user.is_authenticated:
        return redirect("archive")

    if request.method == "POST":
        form = LoginUserForm(request=request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect("archive")
    else:
        form = LoginUserForm(request=request)

    return render(request, "articles/login.html", {"form": form})


def logout_user(request):
    auth_logout(request)
    return redirect("archive")