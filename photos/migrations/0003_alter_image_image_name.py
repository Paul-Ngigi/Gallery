# Generated by Django 3.2.3 on 2021-05-17 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_alter_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_name',
            field=models.CharField(max_length=30),
        ),
    ]