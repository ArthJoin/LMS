# Generated by Django 5.0.4 on 2024-04-15 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(default='default.png', null=True, upload_to='profile_pictures/%y/%m/%d/'),
        ),
    ]