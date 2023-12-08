from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('posts', views.posts, name='posts'),
    path('users', views.users, name='users'),
    path('comments', views.comments, name='comments'),
    path('categories', views.categories, name='categories'),
    path('details/<int:id>', views.blogdetails, name='detail')

]
