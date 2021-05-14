from django.contrib import admin
from .models import User, Image, ImageLocation, ImageCategory

# Register your models here.
admin.site.register(User)
admin.site.register(Image)
admin.site.register(ImageLocation)
admin.site.register(ImageCategory)