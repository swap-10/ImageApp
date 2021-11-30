from django.shortcuts import redirect, render
from cloudinary.forms import cl_init_js_callbacks
import cloudinary
from django.urls import reverse
from .models import Photo
from cars import models as cmodels
from .forms import PhotoForm
from django.db.models.signals import post_delete
from django.dispatch.dispatcher import receiver
# Create your views here.

def upload(request):
    context = {'form': PhotoForm()}
    if (request.method == 'POST'):
        form = PhotoForm(request.POST, request.FILES)
        context['posted'] = form.instance
        if form.is_valid():
            form = form.save(commit=False)
            form.owner = cmodels.Profile.objects.get(pk=request.user.pk)
            form.save()
    
    return render(request, 'upload.html', context)

def images(request):
    if request.user.is_authenticated:
        defaults = dict(format="jpg", height=480, width=480)
        context = {'photos': Photo.objects.filter(owner=cmodels.Profile.objects.get(pk=request.user.pk).pk), 'formatting':defaults}
        return render(request, 'images.html', context)
    else:
        return redirect(reverse('login'))

def delete(request, id):
    item = Photo.objects.get(pk=id)
    print(id)
    if request.user.pk == item.owner_id:
        print(id)
        cloudinary.uploader.destroy(item.image.public_id, invalidate=True)
        Photo.objects.filter(id=id).delete()
        return redirect(reverse('images'))
    else:
        return redirect(reverse('home'))
