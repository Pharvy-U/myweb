from django.shortcuts import render
from django.http import HttpResponse


def home(requests):
    return HttpResponse("This is the home page")


def port(request):
    return HttpResponse("This is the portfolio page")


def about_me(request):
    return HttpResponse("This is the about page")


def blog(request):
    return HttpResponse("This is my blog page")


def blog_single(request):
    return HttpResponse("This is a single blog")


def portfolio_single(request):
    return HttpResponse("This is where i display a project information")


def contact(request):
    return HttpResponse("This is the contact page")