from datetime import date
from django.shortcuts import redirect, render
from demoapp.models import Department,Employee
from django.core.paginator import Paginator
from demoapp.forms import EmployeeForm
from django.contrib import messages


# Create your views here.

def index(request):
    context = {
        'title':'home'
    }
    return render(request, 'demoapp/index.html', context)

def list(request):
    emp = Employee.objects.all()
    # emp = Employee.objects.order_by('-id')
    
    paginator = Paginator(emp,8)
    page=request.GET.get('page')
    employee=paginator.get_page(page)
    context = {'employee': employee, 'title':'List Employee'}
    return render(request, 'demoapp/list.html', context)

def create(request):
    if request.method == 'POST':
        form=EmployeeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Data Created Successfully')
            return redirect('list')    
    else:
       form =EmployeeForm()
    context = {'title':'Create Employee','form':form}
    return render(request, 'demoapp/empform.html', context)

def view_emp(request,id):
    emp=Employee.objects.get(pk=id)
    form=EmployeeForm(request.POST or None,instance=emp)
    context = {'title':'View Employee','form':form,'emp': emp}
    return render(request, 'demoapp/view.html', context)

def edit(request,id):
    if request.method == 'POST':
        emp=Employee.objects.get(pk=id)
        form=EmployeeForm(request.POST,request.FILES,instance=emp)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        emp=Employee.objects.get(pk=id)
        form=EmployeeForm(request.POST or None,instance=emp)
        context = {'title':'Edit Employee','form':form,'emp':emp}
        return render(request, 'demoapp/empform.html', context)    
                