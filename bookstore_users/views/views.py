from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


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
