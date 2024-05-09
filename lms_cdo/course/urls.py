from django.urls import path
from . import views


urlpatterns = [
    path('course/<int:course_id>/', views.course, name='course'),
    path('course/fetch_content/', views.fetch_content, name='fetch_content'),
]