from django.urls import path
from .views import RegisterView, LoginView, ProfileView, TestUserView

urlpatterns = [
    path("register", RegisterView.as_view(), name="register"),
    path("login", LoginView.as_view(), name="login"),
    path("profile", ProfileView.as_view(), name="profile"),
    path("test-user/", TestUserView.as_view(), name="test_user"),
]
