from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def profile(request):
    return HttpResponse('شما وارد شدید!')
