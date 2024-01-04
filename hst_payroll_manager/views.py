import io
import xlsxwriter
from django.urls import reverse
from django.http import FileResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Max, Subquery, OuterRef
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from .models import Employee, Department, Tax, Position, Salary, EmployeeAllowance, EmployeeDeduction, EmployeePercentageDeduction, Payroll, Allowance, Deduction
from .forms import DepartmentForm, PositionForm, TaxForm, DeductionForm, AllowanceForm, EmployeeForm, SalaryForm, EmployeeAllowanceForm, EmployeeDeductionForm, EmployeePercentageDeductionForm
from .utils import list_payroll_days

@login_required(login_url='login')
def dashboard(request):
    employees = Employee.objects.all().order_by('first_name')
    departments = Department.objects.all()
    payrolls = Payroll.objects.all()
    total_gross_pay = 0
    total_net_pay = 0
    total_tax = 0
    for payroll in payrolls:
        total_gross_pay += payroll.total_gross_salary
        total_net_pay += payroll.net_salary
        total_tax += payroll.total_tax
    context = {
        'employees': employees,
        'departments': departments,
        'total_gross_pay': f'{total_gross_pay:,}',
        'total_net_pay': f'{total_net_pay:,}',
        'total_tax': f'{total_tax:,}'
    }
    return render(request, 'index.html', context)

@login_required(login_url='login')
def create_department(request):
    form = DepartmentForm()
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully created a Department')
            return redirect('create-department')
    context = {'form': form}  
    return render(request, 'departments-from.html', context)

@login_required(login_url='login')
def update_department(request, pk):
    department = Department.objects.get(id=pk)
    form = DepartmentForm(instance=department)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully updated a Department')
            return redirect('departments')
    context = {'form': form}  
    return render(request, 'departments-from.html', context)

@login_required(login_url='login')
def delete_department(request, pk):
    department = Department.objects.get(id=pk)
    department.delete()
    return redirect('departments')

@login_required(login_url='login')
def departments(request):
    departments = Department.objects.all()
    context = {
        'departments': departments
    }
    return render(request, 'departments.html', context)

@login_required(login_url='login')
def create_position(request):
    form = PositionForm()
    if request.method == 'POST':
        form = PositionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully Created a Position')
            return redirect('create-position')
    context = {'form': form}
    return render(request, 'positions-from.html', context)

@login_required(login_url='login')
def update_position(request, pk):
    position = Position.objects.get(id=pk)
    form = PositionForm(instance=position)
    if request.method == 'POST':
        form = PositionForm(request.POST, instance=position)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully Updated a Position')
            return redirect('positions')
    context = {'form': form}
    return render(request, 'positions-from.html', context) 

@login_required(login_url='login')
def delete_position(request, pk):
    position = Position.objects.get(id=pk)
    position.delete()
    return redirect('positions')

@login_required(login_url='login')
def positions(request):
    positions = Position.objects.all()
    context = {
        'positions': positions
    }
    return render(request, 'positions.html', context)

@login_required(login_url='login')
def create_tax_rule(request):
    form = TaxForm()
    if request.method == 'POST':
        form = TaxForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully Created a Tax Rule')
            return redirect('create-tax-rule')
    context = {'form': form}
    return render(request, 'tax-form.html', context)   

@login_required(login_url='login')
def update_tax_rule(request, pk):
    tax = Tax.objects.get(id=pk)
    form = TaxForm(instance=tax)
    if request.method == 'POST':
        form = TaxForm(request.POST, instance=tax)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully Updated a Tax Rule')
            return redirect('taxes')
    context = {'form': form}
    return render(request, 'tax-form.html', context) 

@login_required(login_url='login')
def delete_tax_rule(request, pk):
    tax = Tax.objects.get(id=pk)   
    tax.delete()
    return redirect('taxes')

@login_required(login_url='login')
def taxes(request):
    taxes = Tax.objects.all()
    context = {
        'taxes': taxes
    }      
    return render(request, 'taxes.html', context)

@login_required(login_url='login')
def allowances(request):
    allowances = Allowance.objects.all()
    context = {
        'allowances': allowances
    }
    return render(request, 'allowances.html', context)

@login_required(login_url='login')
def create_allowances(request):
    form = AllowanceForm()
    if request.method == 'POST':
        form = AllowanceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully Created an Allowance')
            return redirect('create-allowances')
    context = {'form': form}
    return render(request, 'allowances-form.html', context) 

@login_required(login_url='login')
def update_allowances(request, pk):
    allowance = Allowance.objects.get(id=pk)
    form = AllowanceForm(instance=allowance)
    if request.method == 'POST':
        form = AllowanceForm(request.POST, instance=allowance)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully Updated an Allowance')
            return redirect('allowances')
    context = {'form': form}
    return render(request, 'allowances-form.html', context)

@login_required(login_url='login')
def delete_allowance(request, pk):
    allowance = Allowance.objects.get(id=pk)
    allowance.delete()
    return redirect('allowances')

@login_required(login_url='login')
def deductions(request):
    deductions = Deduction.objects.all()
    context = {
        'deductions': deductions
    }
    return render(request, 'deductions.html', context)

@login_required(login_url='login')
def create_deductions(request):
    form = DeductionForm()
    if request.method == 'POST':
        form = DeductionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully Created a Deduction')
            return redirect('create-deductions')
    context = {'form': form}
    return render(request, 'deductions-form.html', context) 

@login_required(login_url='login')
def update_deductions(request, pk):
    deduction = Deduction.objects.get(id=pk)
    form = DeductionForm(instance=deduction)
    if request.method == 'POST':
        form = DeductionForm(request.POST, instance=deduction)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully Updated a Deduction')
            return redirect('deductions')
    context = {'form': form}
    return render(request, 'deductions-form.html', context) 

@login_required(login_url='login')
def delete_deduction(request, pk):
    deduction = Deduction.objects.get(id=pk)
    deduction.delete()
    return redirect('deductions')

@login_required(login_url='login')
def add_employees(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully Created an Employee')
            return redirect('add-employees')
    context = {'form': form}
    return render(request, 'employees-form.html', context)

@login_required(login_url='login')
def update_employee(request, pk):
    employee = Employee.objects.get(id=pk)
    form = EmployeeForm(instance=employee)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully Updated an Employee')
            return redirect(reverse('update-employee', kwargs={'pk': pk}))
    context = {'form': form}
    return render(request, 'employees-form.html', context)

@login_required(login_url='login')
def delete_employee(request, pk):
    employee = Employee.objects.get(id=pk)
    employee.delete()
    return redirect('employees')

@login_required(login_url='login')
def employees(request):
    employees = Employee.objects.all().order_by('first_name')
    context = {
        'employees': employees
    }
    return render(request, 'employees.html', context)

@login_required(login_url='login')
def add_salaries(request):
    form = SalaryForm()
    if request.method == 'POST':
        form = SalaryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully Created a Salary')
            return redirect('add-salaries')
    context = {'form': form}
    return render(request, 'salaries-form.html', context)

@login_required(login_url='login')
def update_salary(request, pk):
    salary = Salary.objects.get(id=pk)
    form = SalaryForm(instance=salary)
    if request.method == 'POST':
        form = SalaryForm(request.POST, instance=salary)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully Updated a Salary')
            return redirect(reverse('salary-detail', kwargs={'pk': pk}))
    context = {'form': form}
    return render(request, 'salaries-form.html', context)

@login_required(login_url='login')
def delete_salary(request, pk):
    salary = Salary.objects.get(id=pk)
    salary.delete()
    return redirect('salaries')

@login_required(login_url='login')
def salaries(request):
    salaries = Salary.objects.all()
    context = {
        'salaries': salaries
    }
    return render(request, 'salaries.html', context)

@login_required(login_url='login')
def salary_detail(request, pk):
    request.session['salary_id'] = pk
    employee_salary = Salary.objects.get(id=pk)
    employee_id = employee_salary.employee.id
    employee_allowances = EmployeeAllowance.objects.filter(employee=employee_salary.employee)
    employee_deductions = EmployeeDeduction.objects.filter(employee=employee_salary.employee)
    employee_percentage_deductions = EmployeePercentageDeduction.objects.filter(employee=employee_salary.employee)
    context = {'employee_salary': employee_salary, 'employee_allowances': employee_allowances, 'employee_deductions': employee_deductions, 'employee_percentage_deductions': employee_percentage_deductions, 'employee_id': employee_id}
    return render(request, 'salary-detail.html', context)

@login_required(login_url='login')
def add_employee_allowance(request, pk):
    form = EmployeeAllowanceForm()
    employee = Employee.objects.get(id=pk)
    salary_id = request.session.get('salary_id')
    if request.method == 'POST':
        form = EmployeeAllowanceForm(request.POST)
        if form.is_valid():
            allowance = form.save(commit=False)
            allowance.employee = employee
            allowance.save()
            messages.success(request, 'You have successfully Created an Employee Allowance')
            return redirect(reverse('add-employee-allowance', kwargs={'pk': pk}))

    context = {'form': form, 'employee': employee, 'salary_id': salary_id}
    return render(request, 'employee-allowance-form.html', context)

@login_required(login_url='login')
def update_employee_allowance(request, pk):
    employee_allowance = EmployeeAllowance.objects.get(id=pk)
    form = EmployeeAllowanceForm(instance=employee_allowance)
    employee = employee_allowance.employee
    salary_id = request.session.get('salary_id')
    if request.method == 'POST':
        form = EmployeeAllowanceForm(request.POST, instance=employee_allowance)
        if form.is_valid():
            allowance = form.save(commit=False)
            allowance.employee = employee
            allowance.save()
            messages.success(request, 'You have successfully Updated an Employee Allowance')
            return redirect(reverse('salary-detail', kwargs={'pk': salary_id}))

    context = {'form': form, 'employee': employee, 'salary_id': salary_id}
    return render(request, 'employee-allowance-form.html', context)

@login_required(login_url='login')
def delete_employee_allowance(request, pk):
    salary_id = request.session.get('salary_id')
    allowance = EmployeeAllowance.objects.get(id=pk)
    allowance.delete()
    return redirect(reverse('salary-detail', kwargs={'pk': salary_id}))

@login_required(login_url='login')
def add_employee_deduction(request, pk):
    form = EmployeeDeductionForm()
    employee = Employee.objects.get(id=pk)
    salary_id = request.session.get('salary_id')
    if request.method == 'POST':
        form = EmployeeDeductionForm(request.POST)
        if form.is_valid():
            deduction = form.save(commit=False)
            deduction.employee = employee
            deduction.save()
            messages.success(request, 'You have successfully Created an Employee Deduction')
            return redirect(reverse('add-employee-deduction', kwargs={'pk': pk}))
    context = {'form': form, 'employee': employee, 'salary_id': salary_id}
    return render(request, 'employee-deduction-form.html', context)

@login_required(login_url='login')
def update_employee_deduction(request, pk):
    employee_deduction = EmployeeDeduction.objects.get(id=pk)
    form = EmployeeDeductionForm(instance=employee_deduction)
    employee = employee_deduction.employee
    salary_id = request.session.get('salary_id')
    if request.method == 'POST':
        form = EmployeeDeductionForm(request.POST, instance=employee_deduction)
        if form.is_valid():
            deduction = form.save(commit=False)
            deduction.employee = employee
            deduction.save()
            messages.success(request, 'You have successfully Updated an Employee Deduction')
            return redirect(reverse('salary-detail', kwargs={'pk': salary_id}))

    context = {'form': form, 'employee': employee, 'salary_id': salary_id}
    return render(request, 'employee-allowance-form.html', context)

@login_required(login_url='login')
def delete_employee_deduction(request, pk):
    salary_id = request.session.get('salary_id')
    deduction = EmployeeDeduction.objects.get(id=pk)
    deduction.delete()
    return redirect(reverse('salary-detail', kwargs={'pk': salary_id}))

@login_required(login_url='login')
def add_employee_percentage_deduction(request, pk):
    form = EmployeePercentageDeductionForm()
    salary_id = request.session.get('salary_id')
    employee = Employee.objects.get(id=pk)
    if request.method == 'POST':
        form = EmployeePercentageDeductionForm(request.POST)
        if form.is_valid():
            deduction = form.save(commit=False)
            deduction.employee = employee
            deduction.save()
            messages.success(request, 'You have successfully Created an Employee Percentage Deduction')
            return redirect(reverse('add-employee-percentage-deduction', kwargs={'pk': pk}))
    context = {'form': form, 'employee': employee, 'salary_id': salary_id}
    return render(request, 'employee-percentage-deduction-form.html', context)

@login_required(login_url='login')
def update_employee_percentage_deduction(request, pk):
    employee_deduction = EmployeePercentageDeduction.objects.get(id=pk)
    form = EmployeePercentageDeductionForm(instance=employee_deduction)
    employee = employee_deduction.employee
    salary_id = request.session.get('salary_id')
    if request.method == 'POST':
        form = EmployeePercentageDeductionForm(request.POST, instance=employee_deduction)
        if form.is_valid():
            deduction = form.save(commit=False)
            deduction.employee = employee
            deduction.save()
            messages.success(request, 'You have successfully Updated an Employee Percentage')
            return redirect(reverse('salary-detail', kwargs={'pk': salary_id}))

    context = {'form': form, 'employee': employee, 'salary_id': salary_id}
    return render(request, 'employee-allowance-form.html', context)

@login_required(login_url='login')
def delete_employee_percentage_deduction(request, pk):
    salary_id = request.session.get('salary_id')
    deduction = EmployeePercentageDeduction.objects.get(id=pk)
    deduction.delete()
    return redirect(reverse('salary-detail', kwargs={'pk': salary_id}))

@login_required(login_url='login')
def generate_payroll(request):
    dates_list = list_payroll_days(request)   
    try:
        latest_timestamps = Payroll.objects.filter(
            employee=OuterRef('employee')
        ).values('employee').annotate(latest_timestamp=Max('created_on')).values('latest_timestamp')
        displayed_payrolls = Payroll.objects.filter(
        created_on__in=Subquery(latest_timestamps)).order_by('employee')
    except:
        displayed_payrolls = Payroll.objects.all()
        
    if request.method == 'POST':
        allowance_string = ''
        deduction_string = ''
        percentage_deduction_string = ''
        from_date = request.POST['from_date']
        to_date = request.POST['to_date']
        salaries = Salary.objects.all()
        if not Payroll.objects.filter(from_date=from_date, to_date=to_date):
            for salary in salaries:
                total_gross_salary = salary.gross_salary
                pension_contribution = salary.pension_contribution
                total_deduction = 0
                net_salary = 0
                employee_allowances = EmployeeAllowance.objects.filter(employee=salary.employee)
                employee_deductions = EmployeeDeduction.objects.filter(employee=salary.employee)
                employee_percentage_deductions = EmployeePercentageDeduction.objects.filter(employee=salary.employee)
                for allowance in employee_allowances:
                    total_gross_salary += allowance.amount
                    allowance_string += f'{allowance.allowance.allowance_name} = {allowance.amount:,} ETB '
                for deduction in employee_deductions:
                    total_deduction += deduction.amount
                    deduction_string += f'{deduction.deduction.deduction_name} = {deduction.amount:,} ETB '
                for percentage_deduction in employee_percentage_deductions:
                    total_deduction += salary.gross_salary * (percentage_deduction.deduction_percentage / 100)
                    percentage_deduction_string += f'{percentage_deduction.deduction.deduction_name} = {percentage_deduction.deduction_percentage} % '
                tax = Tax.objects.filter(initial_range__lte=total_gross_salary, final_range__gte=total_gross_salary).first()
                tax_calculated = (total_gross_salary * (tax.tax_rate / 100)) - tax.deduction
                net_salary = total_gross_salary - tax_calculated - pension_contribution - total_deduction
                payroll = Payroll.objects.create(
                        employee = salary.employee,
                        from_date = from_date,
                        to_date = to_date,
                        total_gross_salary=total_gross_salary,
                        total_tax = tax_calculated,
                        total_deduction = total_deduction,
                        pension_contribution = pension_contribution,
                        net_salary = net_salary
                )
                payroll_message_subject = 'Payslip'
                payroll_message = render_to_string('email/payroll-email.html', {
                    'employee': salary.employee,
                    'from_date': from_date,
                    'to_date': to_date,
                    'gross_salary': f'{salary.gross_salary:,} ETB',
                    'total_gross_salary': f'{total_gross_salary:,} ETB',
                    'total_tax': f'{tax_calculated:,} ETB',
                    'total_deduction': f'{total_deduction:,} ETB',
                    'pension_contribution': f'{pension_contribution:,} ETB',
                    'net_salary': f'{float(net_salary):,} ETB',
                    'allowance_string': allowance_string,
                    'deduction_string': deduction_string,
                    'percentage_deduction_string': percentage_deduction_string
                })
                employee_email = salary.employee.email
                send_email = EmailMessage(payroll_message_subject, payroll_message, to=[employee_email])
                payroll.save()
                send_email.send()
    context = {"dates_list": dates_list, "displayed_payrolls": displayed_payrolls}
    return render(request, 'payroll-form.html', context)

@login_required(login_url='login')
def payroll_detail(request, pk):
    payroll = Payroll.objects.get(id=pk)
    employee = payroll.employee
    employee_salary = Salary.objects.get(employee=employee)
    employee_allowances = EmployeeAllowance.objects.filter(employee=employee)
    employee_deductions = EmployeeDeduction.objects.filter(employee=employee)
    employee_percentage_deductions = EmployeePercentageDeduction.objects.filter(employee=employee)
    context = {
        'payroll': payroll,
        'employee': employee,
        'employee_salary': employee_salary,
        'employee_allowances': employee_allowances,
        'employee_deductions': employee_deductions,
        'employee_percentage_deductions': employee_percentage_deductions
    }
    return render(request, 'payroll-detail.html', context)


@login_required(login_url='login')
def export_payroll_report(request):
    try:
        latest_timestamps = Payroll.objects.filter(
            employee=OuterRef('employee')
        ).values('employee').annotate(latest_timestamp=Max('created_on')).values('latest_timestamp')
        payrolls = Payroll.objects.filter(
        created_on__in=Subquery(latest_timestamps)).order_by('employee')
        buffer = io.BytesIO()
        workbook = xlsxwriter.Workbook(buffer)
        cell_format = workbook.add_format({'bold': True})
        worksheet = workbook.add_worksheet()
        worksheet.set_column(0,5,30)
        worksheet.write('A1', 'Employee', cell_format)
        worksheet.write('B1', 'From', cell_format)
        worksheet.write('C1', 'To', cell_format)
        worksheet.write('D1', 'Total Gross Salary', cell_format)
        worksheet.write('E1', 'Total Tax', cell_format)
        worksheet.write('F1', 'Pension Contribution', cell_format)
        worksheet.write('F1', 'Total Deduction', cell_format)
        worksheet.write('F1', 'Net Salary', cell_format)
        n = 2
        for i in payrolls:
            worksheet.write(f'A{n}', str(i.employee))
            worksheet.write(f'B{n}', str(i.from_date))
            worksheet.write(f'C{n}', str(i.to_date))
            worksheet.write(f'D{n}', f'{i.total_gross_salary:,} ETB')
            worksheet.write(f'E{n}', f'{i.total_tax:,} ETB')
            worksheet.write(f'F{n}', f'{i.pension_contribution:,} ETB')
            worksheet.write(f'F{n}', f'{i.total_deduction:,} ETB')
            worksheet.write(f'F{n}', f'{i.net_salary:,} ETB')
            n += 1
        workbook.close()
        buffer.seek(0)
        return FileResponse(buffer, as_attachment=True, filename='payroll_report.xlsx')
    except:
        return redirect('payroll-form')
    
# def filter_payroll(request):
    payrolls = Payroll.objects.all()
    
    from_date_list = []
    to_date_list = []
    dates_list = []
    for payroll in payrolls:
        from_date_list.append(payroll.from_date.strftime("%d-%b-%y"))
        to_date_list.append(payroll.to_date.strftime("%d-%b-%y"))
    merged_list = list(zip(from_date_list, to_date_list))
    set_list = list(set(merged_list))
    dates_list = [list(pair) for pair in set_list] 
    
    
    try:
        latest_timestamps = Payroll.objects.filter(
            employee=OuterRef('employee')
        ).values('employee').annotate(latest_timestamp=Max('created_on')).values('latest_timestamp')
        displayed_payrolls = Payroll.objects.filter(
        created_on__in=Subquery(latest_timestamps)).order_by('employee')
    except:
        displayed_payrolls = Payroll.objects.all()
        
    if request.method == 'POST':
        if request.POST['dates_form'] == 'dates_form':
            keyword = request.POST['keyword']
            print(keyword)
            

    context = {"dates_list": dates_list, "displayed_payrolls": displayed_payrolls}
    return render(request, 'payroll-form.html', context)