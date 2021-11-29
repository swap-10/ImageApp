from django.shortcuts import render
from cloudinary.forms import cl_init_js_callbacks
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