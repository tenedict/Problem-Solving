"""pjt0926실습 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from practices import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("is-odd-even/<int:number>", views.oddeven),
    path("cal/<int:first>/<int:second>", views.cal),
    path("pl/", views.pl),
    path("pl1/", views.pl1),
    path("lo/",views.lo),
    path("lo1/",views.lo1),
]
