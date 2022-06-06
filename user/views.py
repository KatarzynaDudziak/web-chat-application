import profile
from django.shortcuts import redirect, render
from user.forms import RegisterForm, UpdateProfileForm, UpdateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def register_user(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('name')
            messages.success(request, "Registration was successful")
            return redirect('login')
        else:
            messages.error(request, form.errors)
    
    return render(request, 'user/register.html', {'form' : form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Wrong password or login')

    return render(request, 'user/login.html')


def logout_user(request):
    logout(request)
    messages.info(request, 'You have been logged out')
    return redirect('/user/login')


@login_required(login_url='user/login')
def user_profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile is updated successfully')
            return redirect('/user/profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'user/profile.html', {'user_form' : user_form, 'profile_form' : profile_form})
