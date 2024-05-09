# Generated by Django 5.0.4 on 2024-04-19 09:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_coursecontent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coursecontent',
            options={'ordering': ['created_at']},
        ),
        migrations.AddField(
            model_name='coursecontent',
            name='course_item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='course_contents', to='course.courseitem'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coursecontent',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default="2021-01-01T00:00:00"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coursecontent',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]