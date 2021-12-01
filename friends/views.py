from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Friend
from django.contrib.auth.models import User
from .forms import FriendForm
from imgs.models import Photo
from cars import models as cmodels
# Create your views here.

def add_friend(request):
    if request.user.is_authenticated:
        form = FriendForm()
        if (request.method == 'POST'):
            if Friend.objects.filter(user=request.user.pk, friend_id=request.POST.get('friend_id')).exists():
                instance = Friend.objects.get(user=request.user.pk, friend_id=request.POST.get('friend_id'))
                form = FriendForm(request.POST, instance=instance)
                if form.is_valid():
                    form = form.save(commit=False)
                    form.user = request.user
                    print(request.user, request.POST.get('friend_id'), "Exists")
                    form.save()
            else:
                form = FriendForm(request.POST)
                if form.is_valid():
                    form = form.save(commit=False)
                    form.user = request.user
                    form.save()
            form = FriendForm()
            friendlist = Friend.objects.all().filter(user=request.user.pk)
            friendrevlist = Friend.objects.all().filter(friend_id=request.user.pk)
            return render(request, 'friends.html', {'form': form, 'friendlist': friendlist, 'friendrevlist': friendrevlist})
        else:
            friendlist = Friend.objects.all().filter(user=request.user.pk)
            friendrevlist = Friend.objects.all().filter(friend_id=request.user.pk)
            return render(request, 'friends.html', {'form': form, 'friendlist': friendlist, 'friendrevlist': friendrevlist})
    else:
        return redirect(reverse('login'))


def friend_imgs(request, username):
    if request.user.is_authenticated:
        if (Friend.objects.filter(user=User.objects.get(username=username).pk, friend_id=request.user.pk).exists()):
            user = cmodels.Profile.objects.get(pk=User.objects.get(username=username).pk)
            defaults = dict(format="jpg", height=480, width=480)
            context = {'photos': Photo.objects.filter(owner=user), 'formatting':defaults, 'friendname': username}
            return render(request, 'friendposts.html', context)
        else:
            return HttpResponse("<h1>Access Forbidden</h1>")
    else:
        return redirect(reverse('login'))