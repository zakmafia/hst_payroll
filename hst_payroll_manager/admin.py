from django.contrib import admin
from .models import Department, Position, Employee, Tax, Salary, EmployeeAllowance, EmployeeDeduction, EmployeePercentageDeduction ,Allowance, Deduction, Payroll
# Register your models here.

class TaxAdmin(admin.ModelAdmin):
    list_display = ('initial_range', 'final_range', 'tax_rate', 'deduction')
    
    def get_ordering(self, request):
        return ['initial_range']  # sorting in the ascending order of the initial range
    
class PayrollAdmin(admin.ModelAdmin):
    list_display = ('employee', 'from_date', 'to_date', 'total_gross_salary', 'total_tax', 'pension_contribution', 'total_deduction', 'net_salary', 'created_on')
    
    # def get_ordering(self, request):
    #     return ['employee'] 

admin.site.register(Department)
admin.site.register(Position)
admin.site.register(Tax, TaxAdmin)
admin.site.register(Deduction)
admin.site.register(Allowance)
admin.site.register(EmployeeAllowance)
admin.site.register(EmployeeDeduction)
admin.site.register(EmployeePercentageDeduction)
admin.site.register(Employee)
admin.site.register(Salary)
admin.site.register(Payroll, PayrollAdmin)
