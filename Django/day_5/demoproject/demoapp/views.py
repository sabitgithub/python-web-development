from django.shortcuts import render
from demoapp.models import Department,Employee


# Create your views here.

def index(request):
    context = {
        'title':'home'
    }
    return render(request, 'demoapp/index.html', context)

def list(request):
    # employee = Employee.objects.all()
    employee = Employee.objects.order_by('-id')
    context = {'employee': employee, 'title':'List Employee'}
    return render(request, 'demoapp/list.html', context)