from django.urls import path
from django.urls import include
from . import views
urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("register", views.register, name="register"),
    path("profile", views.profile, name="profile"),
    path("change_password/", views.change_password, name="change_password"),
]
