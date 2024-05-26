from django.contrib import admin
from .models import Category, Course, CourseProgress


# Register your models here.
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(CourseProgress)