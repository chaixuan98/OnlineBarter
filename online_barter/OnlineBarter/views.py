from django.shortcuts import render,redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


# Create your views here.
def registeraccount(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to login')
            return redirect('loginaccount')
    else:
        form = UserRegisterForm()
    return render(request, 'code/register.html', {'form': form})


def loginaccount(request):
    return render(request,'code/login.html')


def logoutaccount(request):
    logout(request)
    return redirect('index')

@login_required
def updateprofile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your profile has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'code/settings.html', context)

    #return render(request, 'code/settings.html')

def cart(request):
    return render(request,'code/cart.html')

def exchange(request):
    return render(request,'code/exchange.html')

def favourite(request):
    return render(request,'code/favourite.html')

def index(request):
    return render(request,'code/index.html')

def message(request):
    return render(request,'code/message.html')

def detail(request):
    return render(request,'code/product detail.html')

def product(request):
    return render(request,'code/product.html')

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'code/profile.html', context)

def itemlist(request):
    return render(request,'code/item list.html')

def itemform(request):
    
    return render(request,'code/item form.html')

def delete(request):
    return 
