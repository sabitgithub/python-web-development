from random import choices
from django.db import models
from datetime import datetime

# Create your models here.

class Department(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField('Department Name',max_length=100)
    
    def __str__(self):
        return self.name
    
    
class Employee(models.Model):
    
    DESIGNATION_CHOISE=[
        ('Develper','Developer'),
        ('Network Engr','Network Engr'),
        ('Database Administrator','Database Administrator'),
        ('Server Engineer','Server Engineer'),
        
        ]
    
    id=models.AutoField(primary_key=True)
    name=models.CharField('Employee Name',max_length=100)
    email=models.CharField('Email',max_length=100)   
    address=models.CharField('Address',max_length=100)
    doj=models.DateField('Date Of Joining',default=datetime.now,blank=True)   
    phone=models.CharField('Employee Phone',max_length=15)
    designation=models.CharField('Designation',max_length=50,choices=DESIGNATION_CHOISE,default='Developer')
    salary=models.DecimalField('Employee Salary',max_digits=8,decimal_places=2,blank=True,null=True)
    photo=models.FileField('Employee Photo',upload_to='employee',default='employee/blank.jpg',blank=True)
    department=models.ForeignKey(Department, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
       