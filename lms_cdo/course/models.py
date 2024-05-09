from django.db import models
from lms.models import Course
from tinymce.models import HTMLField

# Create your models here.
class CourseItem(models.Model):
    course = models.ForeignKey(Course, related_name='content_items', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, null=True, blank=True)
    order = models.PositiveIntegerField()
    

    class Meta:
        ordering = ['course', 'parent__id', 'order', 'id']  # Сортировка для сохранения порядка пунктов

    def __str__(self):
        return self.title

    def is_root(self):
        return self.parent is None


class CourseContent(models.Model):
    content = HTMLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    course_item = models.ForeignKey(
        CourseItem, 
        related_name='course_contents', 
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['created_at']  # Сортировка по времени создания для удобства отслеживания

    def __str__(self):
        return f"Content for {self.course_item.title}"

