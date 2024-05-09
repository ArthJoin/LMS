# Generated by Django 5.0.4 on 2024-04-19 10:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_alter_coursecontent_course_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursecontent',
            name='course_item',
        ),
        migrations.RemoveField(
            model_name='courseitem',
            name='url',
        ),
        migrations.AddField(
            model_name='courseitem',
            name='course_item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='course_items', to='course.coursecontent'),
            preserve_default=False,
        ),
    ]