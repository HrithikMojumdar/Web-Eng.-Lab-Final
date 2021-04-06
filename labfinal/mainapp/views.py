from django.shortcuts import render,HttpResponse,redirect , get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User
from . models import *

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request =request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username = username, password = password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Invalid Username and password')
        else:
            messages.error(request, 'Invalid Username and password')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form}) 

def logout_user(request):
    logout(request)
    return redirect('/')

from .forms import RegistrationForm
def user_register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form':form})

def index(request):
    return render(request, 'index.html')


def userProfile(request):
    profile = get_object_or_404(UserProfile,user = request.user)
    return render(request, 'profile.html', {'profile':profile})

def displayProduct(request):
    products = product.objects.all()
    return render(request, 'products.html',{'products':products})

def Grocery(request):
    products = product.objects.filter(category__id='3')
    return render(request, 'products.html',{'products':products})

def Dress(request):
    products = product.objects.filter(category__id='4')
    return render(request, 'products.html',{'products':products})

def Electronics(request):
    products = product.objects.filter(category__id='5')
    return render(request, 'products.html',{'products':products})

from . forms import userProfileForm
def profileedit(request):
    try:
        instance = UserProfile.objects.get(user = request.user)
    except UserProfile.DoesNotExist:
        instance = None

    if request.method == "POST":
        if instance:
            form = userProfile(request.POST, request.FILES, instance = instance)
        else:
            form = userProfile(request.POST, request.FILES)
        
        if form.is_valid():
            obj = form.save(commit = False)
            obj.user = request.user
            obj.save()
            obj.save_m2m()
            return redirect('profile')
    else:
        form = userProfileForm(instance=instance)
    context = {
        'form' : form 
    }
    return render(request, 'profileCreate.html', context)
