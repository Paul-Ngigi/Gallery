# Generated by Django 3.2.3 on 2021-05-15 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ImageLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('image_name', models.CharField(max_length=10)),
                ('image_description', models.TextField()),
                ('posted_at', models.DateField(auto_now_add=True)),
                ('image_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='photos.imagecategory')),
                ('image_location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='photos.imagelocation')),
            ],
        ),
    ]
