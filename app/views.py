from django.shortcuts import render

from django.http import HttpResponse


def first(request):
    return HttpResponse('<h1>hi this is my first view</h1>')

def second(request):
    return HttpResponse('<h1><marquee>HI IAM SO WEAK AND UNABLE TO WALK AND TALK</marquee><h1>')

def third(request):
    return HttpResponse('<h1> <marquee>would you like to talk to me or else i need to find new friend<marquee></h1>')