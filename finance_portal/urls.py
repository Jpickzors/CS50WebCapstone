
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="dashboard"),
    path("register", views.register, name="register"),
    path("logout", views.logout_view, name="logout"),
    path("login", views.login_view, name="login")
]
