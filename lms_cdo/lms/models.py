from django.db import models
from django.urls import reverse
from django.db.models import Q
from accounts.models import User
from tinymce.models import HTMLField
from django.utils.html import strip_tags



class Session(models.Model):
    session = models.CharField(max_length=200, unique=True)
    is_current_session = models.BooleanField(default=False, blank=True, null=True)
    next_session_begins = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.session



class ActivityLog(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"[{self.created_at}]{self.message}"



# Модель категории курсов
class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True)
    image = models.ImageField(
        upload_to="categories/%y/%m/%d/", default="default.png", null=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Модель курса
class Course(models.Model):
    category = models.ForeignKey(Category, related_name='courses', on_delete=models.SET_NULL, null=True, verbose_name='Категория')
    title = models.CharField(max_length=200, verbose_name='Название')
    short_description = models.TextField(verbose_name='Короткое описание')
    description = HTMLField()
    image = models.ImageField(upload_to='courses/', verbose_name='Изображение')
    duration = models.PositiveIntegerField(verbose_name='Продолжительность (в часах)')
    chapters_count = models.PositiveIntegerField(verbose_name='Количество глав')
    tags = models.ManyToManyField(Tag, related_name='tags', blank=True, verbose_name='Теги')
    rating = models.FloatField(default=0.0)

    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.short_description = strip_tags(self.short_description)
        super(Course, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

# Модель прогресса курса
class CourseProgress(models.Model):
    class CourseStatus(models.TextChoices):
        IN_PROGRESS = 'in_progress', 'В прогрессе'
        COMPLETED = 'completed', 'Закончил'
        PLANNED = 'planned', 'В планах'

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='course_progress', verbose_name='Пользователь')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='progress', verbose_name='Курс')
    chapters_completed = models.PositiveIntegerField(verbose_name='Глав пройдено', default=0)
    status = models.CharField(
        max_length=12,
        choices=CourseStatus.choices,
        default=CourseStatus.PLANNED,
        verbose_name='Статус курса'
    )
    last_accessed = models.DateTimeField(auto_now=True, verbose_name='Последнее посещение')

    def __str__(self):
        return f'{self.user.username} - {self.course.title} - {self.chapters_completed}/{self.course.chapters_count} глав'

    def get_progress_percentage(self):
        if self.course.chapters_count > 0:
            return (self.chapters_completed / self.course.chapters_count) * 100
        return 0

    class Meta:
        unique_together = ('user', 'course')
        verbose_name = 'Прогресс по курсу'
        verbose_name_plural = 'Прогресс по курсам'
