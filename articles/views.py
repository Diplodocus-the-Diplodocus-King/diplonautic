from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Article
from . import forms


def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {'articles': articles})

@login_required(login_url="/accounts/login/")
def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    comments = article.comments.filter(active=True)
    newComment = None
    if request.method == 'POST':
        form = forms.CreateComment(request.POST, request.FILES)
        if form.is_valid():
            newComment = form.save(commit=False)
            newComment.article = article
            newComment.author = request.user
            newComment.save()
    else:
        form = forms.CreateComment()
    return render(request, 'articles/article_detail.html', {
        'article': article,
        'comments': comments,
        'newComment': newComment,
        'form': form
    })

@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            formInstance = form.save(commit=False)
            formInstance.author = request.user
            formInstance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()        
    return render(request, 'articles/article_create.html', {'form': form})

