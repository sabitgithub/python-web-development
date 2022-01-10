from django.shortcuts import render
from django.http import HttpResponse, request

# Create your views here.

def myView1(request):
    return HttpResponse("Hello <strong>World</strong>")

def myView2(request,para1):
    return HttpResponse(f"<h1>Hello</h1> Dear!! {para1}")

def myView3(request,para1,para2):
    return HttpResponse(f"<h1> Hello {para1}. {para2} </h1>")

def index(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')


