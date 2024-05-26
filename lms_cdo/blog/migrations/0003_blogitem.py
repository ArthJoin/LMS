# Generated by Django 5.0.4 on 2024-05-24 21:17

import django.db.models.deletion
import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='blog/%y/%m/%d/')),
                ('discription', tinymce.models.HTMLField()),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blog', verbose_name='BlogItem')),
            ],
        ),
    ]
