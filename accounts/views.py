from django.shortcuts import render


def signup(request) :
    return render(request, 'accounts/signup.html')

def login(request) :
    return render(request, 'accounts/login.html')

def logout(request) :
    # TODO Need to route back to homepage, and logout
    return render(request, 'accounts/signup.html')
