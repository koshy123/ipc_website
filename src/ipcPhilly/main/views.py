from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def main_view(*args, **kwargs):
    return HttpResponse("<h1>Hi World</h1>")