# Generated by Django 5.0.4 on 2024-04-16 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0004_tag_course_rating_course_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='tags',
            field=models.ManyToManyField(null=True, related_name='courses', to='lms.tag'),
        ),
    ]
