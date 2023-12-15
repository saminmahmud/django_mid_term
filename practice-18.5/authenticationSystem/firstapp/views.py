from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

def signup(request):
    if not request.user.is_authenticated :
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Signup Successfully Now Login')
                return redirect('user_login')
        else: 
            form = RegisterForm()
        return render(request, 'signup.html', {'form': form})
    else:
        return redirect('user_login')

def user_login(request):
    if not request.user.is_authenticated :
        if request.method == 'POST':
            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                user_password = form.cleaned_data['password']
                user = authenticate(username=name, password=user_password)
                if user is not None:
                    login(request,user)
                    messages.success(request, 'Logged In Successfully')
                    return redirect('profile')
        else:
            form=AuthenticationForm()
        return render(request, 'login.html', {'form':form})
    else:
        return redirect('profile')
    
@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully')
    return redirect('home')

@login_required
def passChange(request):
    if request.method == 'POST':
        form = PasswordChangeForm( request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password Change Successfully')
            return redirect('profile')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'pass_change.html', {'form' : form})

@login_required
def passChange2(request):
    if request.method == 'POST':
        form = SetPasswordForm( request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password Change Successfully')
            return redirect('profile')
    else:
        form = SetPasswordForm(request.user)
    return render(request, 'pass_change.html', {'form' : form})



