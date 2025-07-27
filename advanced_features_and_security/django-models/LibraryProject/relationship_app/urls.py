from django.urls import path
from . import views

urlpatterns = [
    # --- Role-Based Views ---
    path('admin_view/', views.admin_view, name='admin_view'),
    path('librarian_view/', views.librarian_view, name='librarian_view'),
    path('member_view/', views.member_view, name='member_view'),

    # --- Auth ---
    path('register/', views.register, name='register'),

    # --- Book CRUD URLs ---
    path('add_book/', views.add_book, name='add_book'),              # ✅ checker required
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),  # ✅ checker required
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),  # ✅ checker required
    path('books/', views.book_list, name='book_list'),  # optional listing
]
