# Generated by Django 5.0.4 on 2024-05-27 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blog_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='short_discription',
            field=models.TextField(null=True, verbose_name='Короткое описание'),
        ),
    ]
