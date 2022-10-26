from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from accounts.models import User
from django.contrib import messages

# Create your views here.
def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article = article_form.save(commit = False)
            article.user = request.user
            article.save()
            return redirect('articles:index')
    else:
        article_form = ArticleForm()
    context = {
        'article_form' : article_form
    }
    return render(request, 'articles/create.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()

    context = {
        'article' : article,
        'comments' : article.comment_set.all(),
        'comment_form' : comment_form,
        }
    return render(request, 'articles/detail.html', context)

def comment_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
    return redirect('articles:detail', article.pk)

def comment_delete(request, pk, comment_pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        Comment.objects.get(pk=comment_pk).delete()
        return redirect('articles:detail', pk)
    else:
        messages.warning(request, '작성자만 삭제할 수 있습니다.')
        return redirect('articles:detail', pk)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        Article.objects.get(pk=pk).delete()
        return redirect('articles:index')
    else:
        messages.warning(request, '작성자만 삭제할 수 있습니다.')
        return redirect('articles:index')
from django.http import JsonResponse
def like(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user in article.like.all():
        article.like.remove(request.user)
        is_liked = False
    else:
        article.like.add(request.user)
        is_liked = True
    
    context = {'isLiked': is_liked, 'likeCount': article.like.count()}
    return JsonResponse(context)
