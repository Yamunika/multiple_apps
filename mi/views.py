from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def sharma(request):
    return HttpResponse('<h1>Rohit sharma is the captain of the mumbai Indians')