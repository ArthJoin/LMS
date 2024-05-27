from django.db import models
from accounts.models import User
from tinymce.models import HTMLField
from django.utils.html import strip_tags
from django.db.models import Q




# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = HTMLField()
    short_discription = models.TextField(verbose_name='Короткое описание', null = True)
    image = models.ImageField(upload_to='blogs/%y/%m/%d/', blank=True, verbose_name='Изображение', default='default.png')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True,  related_name='blogs')
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)


    def __str__(self):
        return self.title

    def to_json(self):
        return {
            'title': self.title,
            'content': self.content,
        }
    
    def total_likes(self):
        return self.likes.count()
    
    def total_comments(self):
        return self.comments.count()

class Comments(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='comment_likes', blank=True)

    
    def __str__(self):
        return f'Comment by {self.author} on {self.post}'
    
    def total_likes(self):
        return self.likes.count()