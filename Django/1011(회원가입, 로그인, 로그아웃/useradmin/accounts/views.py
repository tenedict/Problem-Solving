from django.shortcuts import render, redirect
from .forms import CustomerCreationUserForm
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def index(request):
    users = get_user_model().objects.all()
    context = {
        "users": users,
    }

    return render(request, "accounts/index.html", context)


def signup(request):
    if request.method == "POST":
        form = CustomerCreationUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts:index")
    else:
        form = CustomerCreationUserForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = AuthenticationForm()
        context = {
            'form': form,
        }
        return render(request, 'accounts/login.html', context)