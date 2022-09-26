from tkinter import E
from django.shortcuts import render
import random

# Create your views here.
def oddeven(request, number):
    ans = 0
    if number == 0:
        ans = 0
    elif number % 2 == 0:
        ans = "짝"
    else:
        ans = "홀"
    context = {
        "ans": ans,
        "number": number,
    }
    return render(request, "oddeven.html", context)


def cal(request, first, second):
    p = first + second
    m = first - second
    mu = first * second
    d = first // second
    s = first**second

    context = {
        "p": p,
        "m": m,
        "mu": mu,
        "d": d,
        "s": s,
    }

    return render(request, "cal.html", context)


def pl(request):

    return render(request, "pl.html")


def pl1(request):
    plname = request.GET.get("name")
    li_ = [
        "배",
        "떡",
        "똥",
        "바보",
        "신발",
        "멍청이",
        "선풍기",
        "전등",
        "컵",
        "안약",
    ]

    random.seed(plname)

    random.shuffle(li_)

    context = {"plname": request.GET.get("name"), "ppp": li_[0]}
    return render(request, "pl1.html", context)


def lo(request):

    return render(request, "lo.html")


def lo1(request):
    m = int(request.GET.get("lor"))
    d = int(request.GET.get("lor1"))

    li_ = [
        "응가",
        "떡",
        "똥",
        "바보",
        "신발",
        "멍청이",
        "선풍기",
        "전등",
        "컵",
        "안약",
    ]
    ans = []
    for i in range(m):
        a = " "
        for j in range(d):
            a = a + random.choice(li_) + " "
        ans.append(a)

    context = {
        "lor": request.GET.get("lor"),
        "lor1": request.GET.get("lor1"),
        "ans": ans,
    }
    return render(request, "lo1.html", context)
