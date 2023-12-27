from django.shortcuts import render
from .models import Employee

# Create your views here.
def dashboard(request):
    employees = Employee.objects.all()
    context = {
        'employees': employees
    }
    return render(request, 'index.html', context)