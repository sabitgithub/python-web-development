import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demoproject.settings')
from unicodedata import name



import django
django.setup()
from demoapp.models import Department,Employee
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# pip install faker
from faker import Faker


fakegen= Faker()

def add_employee():
    fname=fakegen.name()
    femail=  fakegen.email() 
    faddress=fakegen.address()
    fdoj=fakegen.date()   
    fphone='01745871019'
    fdesignation='Manager'    
    fsalary='10000'
    fdepartment='1'
    
    emp= Employee.objects.get_or_create(
        name=fname,
        email=femail,
        address=faddress,
        doj=fdoj,
        phone=fphone,
        designation=fdesignation,
        salary=fsalary,
        department_id=fdepartment
    )[0]
    return emp


def populateData(n=5):
    for x in range(n):
        emp = add_employee()
        
        
populateData()
print("Done")

# Creating Superuser

user = User.objects.get_or_create(
    username='sabit123',
    password=make_password('123'),
    email='sabit@gmail.com',
    first_name='Waliur Rahman',
    last_name='Sabit',
    is_staff=True,
    is_superuser=True,
    is_active=True
    
)
print('SuperUser Created Successfully')