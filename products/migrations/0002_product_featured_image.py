# Generated by Django 4.1.5 on 2023-02-16 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='featured_image',
            field=models.ImageField(default='null', upload_to='product'),
        ),
    ]