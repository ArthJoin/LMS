# Generated by Django 5.0.4 on 2024-04-16 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0005_alter_course_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, related_name='tags', to='lms.tag', verbose_name='Теги'),
        ),
    ]
