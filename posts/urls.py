from django.urls import path

from . import views
from .apps import PostsConfig


app_name = PostsConfig.name


urlpatterns = [
    path('', views.index, name='index'),
]
