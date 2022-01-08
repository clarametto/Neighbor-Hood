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

# views here.
def index(request):
    current_user = request.user

    profiles = Profile.objects.filter(user_id = current_user.id).all()
    return render(request, 'index.html',{'profiles':profiles,})
    

@login_required(login_url='/accounts/login/')
def create_profile(request):
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
    return render(request, 'create_profile.html', {'form': form}
    )
@login_required(login_url="/accounts/login/")
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    ctx = {"profile": profile}
    return render(request, "profile.html", ctx)

@login_required(login_url="/accounts/login/")
def update_profile(request,id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user = user)
    form = UpdateProfileForm(instance=profile)
    if request.method == "POST":
            form = UpdateProfileForm(request.POST,request.FILES,instance=profile)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.save()
                return redirect('profile')
    ctx = {"form":form}
    return render(request, 'update_profile.html', ctx)

@login_required(login_url="/accounts/login/")
def create_hood(request):
    current_user = request.user
    if request.method == 'POST':
        hood_form = CreateHoodForm(request.POST, request.FILES)
        if hood_form.is_valid():
            hood = hood_form.save(commit=False)
            hood.user = current_user
            hood.save()
        return HttpResponseRedirect('/profile')
    else:
        hood_form = CreateHoodForm()
    context = {'hood_form':hood_form}
    return render(request, 'hood/create_hood.html',context)

@login_required(login_url="/accounts/login/")
def hoods(request):
    current_user = request.user
    hood = NeighbourHood.objects.all().order_by('-id')

    context ={'hood':hood}
    return render(request, 'hood/hood.html', context)


@login_required(login_url="/accounts/login/")
def single_hood(request,name):
    hood = NeighbourHood.objects.get(name=name)
    ctx = {"hood":hood}
    return render(request, 'hood/single_hood.html', ctx)
