from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def main_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    # return HttpResponse("<h1>Hi World</h1>")
    return render(request, "home.html", {})
    
def contact_view(request, *arg, **kwargs):
    return HttpResponse("<h1>Contacts Page</h1>")

def about_view(request, *arg, **kwargs):
    return HttpResponse("<h1>About Page</h1>")

def calendar_view(request, *arg, **kwargs):
    return HttpResponse("<h1>Calendar Page</h1>")