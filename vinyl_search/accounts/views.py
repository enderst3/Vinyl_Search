from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login as generic_login


def login(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)

            if user is not None:  # returns None if Permission Denied
                generic_login(request, user)
                return redirect('/')

    context = {'form': form}
    return render(request, 'login.html', context)


def register(request):
    """
    'Views' are functions that take an HTTP request
    as input and return an HTTP Response as output.
    """
    if request.method == 'GET':
        user_form = UserCreationForm()

    elif request.method == 'POST':
        querydict = request.POST
        user_form = UserCreationForm(data=querydict)

        if user_form.is_valid():
            user = user_form.save(commit=False)

            user.save()

            return redirect('/')

    context = {'user_form': user_form}
    return render(request, 'register.html', context)
