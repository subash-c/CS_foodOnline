from django.http.response import HttpResponse
from django.shortcuts import render

def home(req):
    return render(req,"home.html")