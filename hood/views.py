from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from hood.forms import *
from django.contrib.auth.models import User
from hood.models import *
from django import forms
from django.http.response import Http404, HttpResponseRedirect
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Create your views here.
def index(request):
    current_user = request.user

    profiles = Profile.objects.filter(user_id = current_user.id).all()
    return render(request, 'index.html',{'profiles':profiles,})
    
@login_required(login_url='/accounts/login/')
def update_profile(request):
    current_user = request.user
    form = ProfileForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            prof = form.save(commit=False)
            prof.user = request.user
            prof.save()
            return redirect ('index')
        else:
            form = ProfileForm()
    return render(request, 'create_profile.html', {'form': form})

@login_required(login_url='/accounts/login/')
def profile(request,pk):
    user = User.objects.get(pk = pk)
    profiles = Profile.objects.filter(user = user).all()
    current_user = request.user

    return render(request,'profile.html',{"current_user":current_user, "user":user, "profiles":profiles})
