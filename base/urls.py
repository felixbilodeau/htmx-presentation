from django.urls import path

from . import views
from .apps import BaseConfig


app_name = BaseConfig.name


urlpatterns = [
    path('', views.homepage, name='home'),
    path('empty/', views.empty, name='empty'),
]
