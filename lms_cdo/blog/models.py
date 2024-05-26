from django.db import models
from accounts.models import User
from tinymce.models import HTMLField
from django.utils.html import strip_tags
from django.db.models import Q




# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = HTMLField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='blogs')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def to_json(self):
        return {
            'title': self.title,
            'content': self.content,
        }


