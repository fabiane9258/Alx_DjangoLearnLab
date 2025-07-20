from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    # Optional:
    # path('libraries/<int:library_id>/', views.library_detail, name='library_detail'),
]
