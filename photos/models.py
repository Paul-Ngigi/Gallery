from django.db import models


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return {self.first_name}


class ImageCategory(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return {self.name}


class ImageLocation(models.Model):
    location_name = models.CharField(max_length=30)

    def __str__(self):
        return {self.location_name}


class Image(models.Model):
    image = models.ImageField()
    image_name = models.CharField(max_length=10)
    image_description = models.TextField()
    image_location = models.ForeignKey(ImageLocation, on_delete=models.CASCADE)
    image_category = models.ForeignKey(ImageCategory, on_delete=models.CASCADE)

    def __str__(self):
        return {self.image_name}
