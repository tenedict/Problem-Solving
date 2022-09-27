from django.shortcuts import render

from pjt0926.settings import BASE_DIR
from  .models import Article

# Create your views here.
gb = []

def index(request):
    context = { 'gb' : Article.objects.all()}
    
    return render(request, "articles/index.html",context)


def create(request):
    context = {"content": request.GET.get("content")}
    gb.append(request.GET.get("content"))
    Article.objects.create(content=request.GET.get("content"))

    return render(request, "articles/create.html", context)
