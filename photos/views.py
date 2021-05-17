from django.shortcuts import render
from django.http import HttpResponse
from .models import Image
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def index(request):
    images = Image.objects.all()
    return render(request, 'index.html', {"images": images})


def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_image(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {'message': message, 'images': searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {'message': message})


def view_image(request, image_id):
    try:
        image = Image.objects.get(id=image_id)
        return image

    except ObjectDoesNotExist:
        message = 'Sorry, we could not find what you are looking for'
        return render(request, 'image.html', {'image': image})

