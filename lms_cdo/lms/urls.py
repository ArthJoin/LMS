from django.urls import path
from . import views


urlpatterns = [
    path('catalog', views.catalog, name='catalog'),
    path('catalog/<int:category_id>/', views.catalog_detail, name='catalog_detail'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('unassign-course/<int:course_id>/', views.unassign_course, name='unassign-course'),
    path('assign_course/<int:course_id>/', views.assign_course, name='assign_course'),
    path('learning', views.learning, name='learning'),
]