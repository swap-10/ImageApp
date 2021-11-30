from django.shortcuts import redirect, render
from cloudinary.forms import cl_init_js_callbacks
from django.urls import reverse
from .models import Photo
from cars import models as cmodels
from .forms import PhotoForm
# Create your views here.

def upload(request):
    context = {'form': PhotoForm()}
    if (request.method == 'POST'):
        # instance = Profile.objects.get(pk=request.user.pk)
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