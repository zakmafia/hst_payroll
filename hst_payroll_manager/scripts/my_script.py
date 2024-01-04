from hst_payroll_manager.models import Salary, EmployeeAllowance, EmployeeDeduction, Payroll, Employee, Tax

def run():
    # employee = Employee.objects.get(first_name='Zekarias', last_name='Mesfin')
    
    # salary = Salary.objects.get(employee=employee)
    
    # employee_allowances = EmployeeAllowance.objects.filter(employee=employee)
    
    # print(salary.gross_salary)
    
    # total_gross_salary = salary.gross_salary
    
    # for allowance in employee_allowances:
    #     print(allowance.allowance.allowance_name, allowance.amount)
    #     total_gross_salary += allowance.amount
        
    
    # tax = Tax.objects.filter(initial_range__lte=total_gross_salary, final_range__gte=total_gross_salary).first()
    
    # tax_calculated = (total_gross_salary * (tax.tax_rate / 100)) - tax.deduction
    
    # print(total_gross_salary)
    # print(tax_calculated)
    
    salaries = Salary.objects.all()
    for salary in salaries:
        total_gross_salary = salary.gross_salary
        pension_contribution = salary.pension_contribution
        total_deduction = 0
        net_salary = 0
        employee_allowances = EmployeeAllowance.objects.filter(employee=salary.employee)
        employee_deductions = EmployeeDeduction.objects.filter(employee=salary.employee)
        for allowance in employee_allowances:
            print(allowance.allowance.allowance_name, allowance.amount)
            total_gross_salary += allowance.amount
        for deduction in employee_deductions:
            total_deduction += deduction.amount
        tax = Tax.objects.filter(initial_range__lte=total_gross_salary, final_range__gte=total_gross_salary).first()
        tax_calculated = (total_gross_salary * (tax.tax_rate / 100)) - tax.deduction
        net_salary = total_gross_salary - tax_calculated - pension_contribution - total_deduction
        payroll = Payroll.objects.create(
                employee = salary.employee,
                total_gross_salary=total_gross_salary,
                total_tax = tax_calculated,
                total_deduction = total_deduction,
                pension_contribution = pension_contribution,
                net_salary = net_salary
        )
        payroll.save()
        
        
        
        
       
        
            