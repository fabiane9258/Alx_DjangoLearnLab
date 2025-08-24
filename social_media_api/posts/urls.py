# posts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Example placeholder — you can replace with real views later
    path('', views.index, name='posts-index'),
]
