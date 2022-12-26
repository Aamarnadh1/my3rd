from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('<h1>this is amar1 first view</h1>')

def second(request):
    return HttpResponse('<h2><marquee> this amar1 second view</marquee></h2>')   
