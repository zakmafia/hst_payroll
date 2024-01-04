from .models import Payroll

def list_payroll_days(request):
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
    
    return dates_list
    
    