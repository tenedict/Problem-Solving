from django.urls import path
from . import views

app_name = "fight"

urlpatterns = [
    path("create/", views.create, name="create"),
]
