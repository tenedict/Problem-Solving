from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        "posts": posts,
    }
    return render(request, "posts/index.html", context)


def new(request):
    return render(request, "posts/new.html")


def create(request):
    # DB 저장
    # 파라미터로 날라온 데이터를 DB에 저장
    title = request.GET.get("title")
    content = request.GET.get("content")

    Post.objects.create(title=title, content=content)

    context = {
        "title": title,
        "content": content,
    }

    return render(request, "posts/create.html", context)


def delete(request, pk):
    # pk에 해당하는 글 삭제
    Post.objects.get(id=pk).delete()

    return redirect("posts:index")
