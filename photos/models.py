from django.db import models


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return {self.first_name}

    def save_user(self):
        self.save()

    def delete_user(self):
        self.delete()


class ImageCategory(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return {self.name}

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()


class ImageLocation(models.Model):
    location_name = models.CharField(max_length=30)

    def __str__(self):
        return {self.location_name}

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()


class Image(models.Model):
    image = models.ImageField()
    image_name = models.CharField(max_length=10)
    image_description = models.TextField()
    image_location = models.ForeignKey(ImageLocation, on_delete=models.CASCADE, null=True)
    image_category = models.ForeignKey(ImageCategory, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return {self.image_name}

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(cls, id, image):
        image_update = cls.objects.filter(id=id).update(image=image)

    @classmethod
    def get_image_by_id(cls, id):
        image = Image.objects.filter(id=id)
        return image

    @classmethod
    def search_image(cls, category):
        image = Image.objects.filter(category=category)
        return image

    @classmethod
    def filter_by_location(cls, location):
        image = Image.objects.filter(location=location)
        return image
