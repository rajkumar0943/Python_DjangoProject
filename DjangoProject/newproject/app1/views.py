from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Employee,Department


# Create your views here.
def home(request):
    all_departments = Department.objects.all()
    template = loader.get_template('app1/home.html')
    all_employees = Employee.objects.all()

    data = {
        'all_departments':all_departments,'all_employees' :  all_employees,
    }

    return HttpResponse(template.render(data, request))

def departmentIdView(request, number):
    department = Department.objects.get(id = number)

    template = loader.get_template('app1/departments.html')

    data = {
        'department': department,
    }
    return HttpResponse(template.render(data, request))

def employeeIdView(request, number):
    employee = Employee.objects.get(id = number)

    template = loader.get_template('app1/employees.html')

    data= {
        'employee': employee,
    }
    return HttpResponse(template.render(data, request))














# def apiDesign(request):


#   return HttpResponse("<h1>this is the apiDesign</h1>")
