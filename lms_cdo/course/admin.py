from django.contrib import admin
from .models import CourseItem, CourseContent

# Register your models here.
admin.site.register(CourseItem)
admin.site.register(CourseContent)