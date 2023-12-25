from django.contrib import admin
from .models import Department, Position, Employee, PaymentCurrency
# Register your models here.


admin.site.register(Department)
admin.site.register(Position)
admin.site.register(PaymentCurrency)
admin.site.register(Employee)
