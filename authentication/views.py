from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        # Get form values
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # Check username
        if User.objects.filter(username=username).exists():
            messages.error(request, 'That username is taken')
            return redirect('register')
        else:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'That email is being used')
                return redirect('register')
            else:
                # Looks good
                user = User.objects.create_user(
                    username=username, password=password, email=email)
                # Login after register
                # auth.login(request, user)
                # messages.success(request, 'You are now logged in')
                # return redirect('index')
                user.save()
                messages.success(
                    request, 'You are now registered and can log in')
                return redirect('login')

    else:
        return render(request, 'authentication/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('expenses')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'authentication/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('login')


def reset_password(request):
    return render(request, 'authentication/reset-password.html',)
