# Generated by Django 5.0.4 on 2024-04-19 10:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_alter_coursecontent_course_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursecontent',
            name='course_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_contents', to='course.courseitem'),
        ),
    ]
