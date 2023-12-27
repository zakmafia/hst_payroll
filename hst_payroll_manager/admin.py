from django.contrib import admin
from .models import Department, Position, Employee, Tax, Salary
# Register your models here.

class TaxAdmin(admin.ModelAdmin):
    list_display = ('initial_range', 'final_range', 'tax_rate', 'deduction')
    
    def get_ordering(self, request):
        return ['initial_range']  # sorting in the ascending order of the initial range

admin.site.register(Department)
admin.site.register(Position)
admin.site.register(Tax, TaxAdmin)
admin.site.register(Employee)
admin.site.register(Salary)
