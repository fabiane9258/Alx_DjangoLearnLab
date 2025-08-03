from django.urls import path
from .views import ToDoListCreateView, ToDoRetrieveUpdateDestroyView

urlpatterns = [
    path('todos/', ToDoListCreateView.as_view(), name='todo-list-create'),
    path('todos/<int:pk>/', ToDoRetrieveUpdateDestroyView.as_view(), name='todo-detail'),
]
