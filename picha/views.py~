from django.shortcuts import render, redirect, get_object_or_404

from picha.models import Picture
from picha.forms import PictureForm


def home(request):
    images = Picture.objects.all()
    return render(request, "picha/home.html", {'images': images})


def add_picture(request):
    form = PictureForm()
    if request.method == "POST":
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, "picha/picture_form.html", {'form': form})


def edit_picture(request, id):
    image = get_object_or_404(Picture, pk=id)
    form = PictureForm(instance=image)
    if request.method == "POST":
        form = PictureForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, "picha/picture_form.html", {'form': form})
