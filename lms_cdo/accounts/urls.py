from django.urls import path
from django.urls import include
from . import views
from django.contrib.auth import views as auth_views




urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("register", views.register, name="register"),
    path("profile", views.profile, name="profile"),
    path("change_password/", views.change_password, name="change_password"),
    path("profile/<int:profile_id>/edit/", views.edit_profile, name="edit_profile"),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]

