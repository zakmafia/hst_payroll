from django import forms
from django.forms import ModelForm
from .models import Department, Position, Tax, Allowance, Deduction, Employee, Salary, Payroll, EmployeeAllowance, EmployeeDeduction, EmployeePercentageDeduction

class DateInput(forms.DateInput):
    input_type = 'date'

class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = ['department_name', 'department_description', 'status']
        
    def __init__(self, *args, **kwargs):
        super(DepartmentForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
        
class PositionForm(ModelForm):
    class Meta:
        model = Position
        fields = ['position_name', 'position_description', 'status']
        
    def __init__(self, *args, **kwargs):
        super(PositionForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
            
class TaxForm(ModelForm):
    class Meta:
        model = Tax
        fields = ['initial_range', 'final_range', 'tax_rate', 'deduction']
        
    def __init__(self, *args, **kwargs):
        super(TaxForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
            
class AllowanceForm(ModelForm):
    class Meta:
        model = Allowance
        fields = ['allowance_name', 'is_taxable']
        
    def __init__(self, *args, **kwargs):
        super(AllowanceForm, self).__init__(*args, **kwargs)
        self.fields['allowance_name'].widget.attrs['class'] = 'form-control'   
        self.fields['is_taxable'].widget.attrs['class'] = 'form-check-input'   
            
class DeductionForm(ModelForm):
    class Meta:
        model = Deduction
        fields = ['deduction_name', 'is_taxable']
        labels = {
            'is_taxable': 'Is Taxable'
        }
        
    def __init__(self, *args, **kwargs):
        super(DeductionForm, self).__init__(*args, **kwargs)
        self.fields['deduction_name'].widget.attrs['class'] = 'form-control'   
        self.fields['is_taxable'].widget.attrs['class'] = 'form-check-input'   
        
class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'gender', 'email', 'birthday', 'phone_number', 'country', 'city','department', 'position', 'account_number', 'bank_name', 'date_hired', 'status']
        widgets = {
            'birthday': DateInput()
        }
        
    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['birthday'].widget.attrs['placeholder'] = 'yyyy-mm-dd'
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
            
class SalaryForm(ModelForm):
    class Meta:
        model = Salary
        fields = ['employee', 'total_working_days', 'gross_salary', 'payment_currency', 'foreign_currency_adjustment', 'pension']
        
    def __init__(self, *args, **kwargs):
        super(SalaryForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
            
class EmployeeAllowanceForm(ModelForm):
    class Meta:
        model = EmployeeAllowance
        fields = ['allowance', 'amount', 'payment_currency']
        
    def __init__(self, *args, **kwargs):
        super(EmployeeAllowanceForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
            
class EmployeeDeductionForm(ModelForm):
    class Meta:
        model = EmployeeDeduction
        fields = ['deduction', 'amount', 'payment_currency']
        
    def __init__(self, *args, **kwargs):
        super(EmployeeDeductionForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
            
class EmployeePercentageDeductionForm(ModelForm):
    class Meta:
        model = EmployeePercentageDeduction
        fields = ['deduction', 'deduction_percentage']
        
    def __init__(self, *args, **kwargs):
        super(EmployeePercentageDeductionForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
            
class PayrollForm(ModelForm):
    class Meta:
        model = Payroll
        fields = ['from_date', 'to_date']
        widgets = {
            'from_date': DateInput(),
            'to_date': DateInput()
        }
    
    def __init__(self, *args, **kwargs):
        super(PayrollForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})   
    