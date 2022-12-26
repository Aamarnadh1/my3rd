from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def lucky(request):
    return HttpResponse('<i><h1> this amar2 first view<i><h1>')

def ram(request):
    return HttpResponse('<b><h3> this amar2 second view<b><h3>')
