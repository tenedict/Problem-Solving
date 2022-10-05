from django.urls import path
from . import views

app_name = "record"

urlpatterns = [
    path("", views.book, name="book"),
    path("create/", views.create, name="create"),
    path("<int:pk>/", views.detail, name="detail"),
    path("update/<int:pk>/", views.update, name="update"),
]
