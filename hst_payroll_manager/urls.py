from django.urls import path
from . import views

urlpatterns =  [
    path('', views.dashboard, name='dashboard'),
    
    path('create-department/', views.create_department, name='create-department'),
    path('update-department/<str:pk>/', views.update_department, name='update-department'),
    path('delete-department/<str:pk>/', views.delete_department, name='delete-department'),
    path('departments/', views.departments, name='departments'),
    
    path('create-position/', views.create_position, name='create-position'),
    path('update-position/<str:pk>/', views.update_position, name='update-position'),
    path('delete-position/<str:pk>/', views.delete_position, name='delete-position'),
    path('positions/', views.positions, name='positions'),
    
    path('create-tax-rule/', views.create_tax_rule, name='create-tax-rule'),
    path('update-tax-rule/<str:pk>/', views.update_tax_rule, name='update-tax-rule'),
    path('delete-tax-rule/<str:pk>/', views.delete_tax_rule, name='delete-tax-rule'),
    path('taxes/', views.taxes, name='taxes'),
    
    path('allowances/', views.allowances, name='allowances'),
    path('create-allowances/', views.create_allowances, name='create-allowances'),
    path('update-allowances/<str:pk>/', views.update_allowances, name='update-allowances'),
    path('delete-allowance/<str:pk>/', views.delete_allowance, name='delete-allowance'),
    
    path('deductions/', views.deductions, name='deductions'),
    path('create-deductions/', views.create_deductions, name='create-deductions'),
    path('update-deductions/<str:pk>/', views.update_deductions, name='update-deductions'),
    path('delete-deduction/<str:pk>/', views.delete_deduction, name='delete-deduction'),
    
    path('add-employees/', views.add_employees, name='add-employees'),
    path('update-employee/<str:pk>/', views.update_employee, name='update-employee'),
    path('delete-employee/<str:pk>/', views.delete_employee, name='delete-employee'),
    path('employees/', views.employees, name='employees'),
    
    path('add-salaries/', views.add_salaries, name='add-salaries'),
    path('update-salary/<str:pk>/', views.update_salary, name='update-salary'),
    path('delete-salary/<str:pk>/', views.delete_salary, name='delete-salary'),
    path('salaries/', views.salaries, name='salaries'),
    path('salary-detail/<str:pk>/', views.salary_detail, name='salary-detail'),
    
    path('add-employee-allowance/<str:pk>/', views.add_employee_allowance, name='add-employee-allowance'),
    path('update-employee-allowance/<str:pk>/', views.update_employee_allowance, name='update-employee-allowance'),
    path('delete-employee-allowance/<str:pk>/', views.delete_employee_allowance, name='delete-employee-allowance' ),
    
    path('add-employee-deduction/<str:pk>/', views.add_employee_deduction, name='add-employee-deduction'),
    path('update-employee-deduction/<str:pk>/', views.update_employee_deduction, name='update-employee-deduction'),
    path('delete-employee-deduction/<str:pk>/', views.delete_employee_deduction, name='delete-employee-deduction' ),
    
    path('add-employee-percentage-deduction/<str:pk>/', views.add_employee_percentage_deduction, name='add-employee-percentage-deduction'),
    path('update-employee-percentage-deduction/<str:pk>/', views.update_employee_percentage_deduction, name='update-employee-percentage-deduction'),
    path('delete-employee-percentage-deduction/<str:pk>/', views.delete_employee_percentage_deduction, name='delete-employee-percentage-deduction' ),
    
    path('generate-payroll/', views.generate_payroll, name='generate-payroll'),
    path('payroll-detail/<str:pk>/', views.payroll_detail, name='payroll-detail'),
    
    path('export-payroll-report/', views.export_payroll_report, name='export-payroll-report'),
    
    # path('filter-payroll/', views.filter_payroll, name='filter-payroll')
]