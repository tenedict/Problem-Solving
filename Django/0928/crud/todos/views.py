from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    _todos = Todo.objects.all()
    context = {
        "todos": _todos,
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
