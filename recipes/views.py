from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse('HOME')


def contact(request):
    return HttpResponse('CONTACT')


def about(request):
    return HttpResponse('ABOUT')
