from django.urls import path
from . import views


app_name = 'blogs'


urlpatterns = [
    path('home/', views.ViewAllBlogs.as_view(), name='home'),
    path('create/', views.CreateBlogView.as_view(), name='create_blog'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('edit/<int:blog_id>/', views.EditBlog.as_view(), name='edit_blog'),
    path('delete/<int:blog_id>/', views.DeleteBlog.as_view(), name='delete'),
    path('detail/<int:blog_id>/', views.ViewBlog.as_view(), name='blog_detail'),
]