from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def home_view(request):
    """Home view callable, for the home page."""
    context = {}
    return render(request, 'django_imager/home.html', context=context)


# def login_view(request):
#     return render(request, 'django_imager/login.html')


def account_view(request):
    return render(request, 'django_imager/account.html')
