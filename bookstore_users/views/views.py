# Django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Manager
from bookstore_users.models import User
# Exceptions
from django.db.utils import IntegrityError


def login_view(request):
    LOGIN_TEMPLATE = 'bookstore_users/accounts/login.html'
    if request.method == "POST":
        # The username is actually the email, because we use it to log in.
        # The actual username does not exist. See the User model.
        email = request.POST["email"]
        password = request.POST["password"]

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('inventory:list_create')
        else:
            return render(
                request,
                LOGIN_TEMPLATE,
                context={'error': 'Invalid email or password'}
            )

    return render(request, LOGIN_TEMPLATE)


@login_required
def logout_view(request):
    logout(request)
    return redirect('users:login')


def signup_view(request):
    SIGNUP_TEMPLATE = ''

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']

        if password != password_confirmation:
            context = {'error': 'Passwords do not match'}
            return render(render, SIGNUP_TEMPLATE, context=context)

        try:
            user = User.objects.create_user(
                email=email,
                password=password
            )
        except IntegrityError:
            context = {'error': 'Email is already in use'}
            return render(request, SIGNUP_TEMPLATE, context=context)

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.save()

        return redirect('users:login')

    return render(request, 'bookstore_users/accounts/signup.html')
