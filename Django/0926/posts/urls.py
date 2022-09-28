from django.urls import path
from . import views
# 메인 R 게시슬 목록 /posts
# 작성 C posts/new
# 수정 U
# 삭제 D


app_name = 'posts'
urlpatterns = [
    path("",views.index, name='index'),
    path("new/",views.new, name='new'),
    path('create/', views.create, name='create'),
    path('delete/<int:pk>', views.delete, name='delete')
    ]