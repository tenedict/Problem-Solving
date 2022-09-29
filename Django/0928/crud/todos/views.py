from django.shortcuts import render, redirect
from .models import Todo
from datetime import datetime

# Create your views here.
def index(request):
    _todos = Todo.objects.all()
    today = datetime.now().strftime("%Y-%m-%d")
    print(today)
    context = {
        "todos": _todos,
        "today": today,
    }

    return render(request, "todos/index.html", context)


def create(request):
    content = request.GET.get("content")
    priority = request.GET.get("priority")
    deadline = request.GET.get("deadline")

    Todo.objects.create(content=content, priority=priority, deadline=deadline)
    return redirect("todos:index")


def delete(request, pk):
    Todo.objects.get(id=pk).delete()

    return redirect("todos:index")


def edit(request, pk):
    todo = Todo.objects.get(id=pk)
    if todo.completed:
        todo.completed = False
    else:
        todo.completed = True
    todo.save()

    return redirect("todos:index")


def detail(request, pk):
    todo = Todo.objects.get(id=pk)
    context = {
        "todo": todo,
    }

    return render(request, "todos/detail.html", context)


def detailedit(request, pk):
    todo = Todo.objects.get(id=pk)
    content = request.GET.get("content")
    priority = request.GET.get("priority")
    deadline = request.GET.get("deadline")

    todo.content = content
    todo.priority = priority
    todo.deadline = deadline

    todo.save()

    return redirect("todos:index")
