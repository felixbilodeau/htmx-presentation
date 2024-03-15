from django.urls import path

from . import views
from .apps import PostsConfig


app_name = PostsConfig.name


urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.post_list, name='list'),
    path('create/', views.create, name='create'),
    path('<uuid:pk>/', views.get_post, name='post'),
    path('update/<uuid:pk>', views.update, name='update'),
]
