from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(req):
    # return render(req, "index.html")
    return HttpResponse("<h1>hei there</he>")