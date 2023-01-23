from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def main_view(*args, **kwargs):
    return HttpResponse("<h1>Hi World</h1>")

def contact_view(*arg, **kwargs):
    return HttpResponse("<h1>Contacts Page</h1>")

def about_view(*arg, **kwargs):
    return HttpResponse("<h1>About Page</h1>")

def calendar_view(*arg, **kwargs):
    return HttpResponse("<h1>Calendar Page</h1>")