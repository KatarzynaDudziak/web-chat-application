from django.shortcuts import redirect, render
from user.forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


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
