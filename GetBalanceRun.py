from openpyxl import load_workbook
from datetime import datetime
import GetBalance as Balance
ascii_uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
bal=Balance.GetBalance();
try:
    wb = load_workbook("balance.xlsx");
except FileNotFoundError:
    print("balance.xlsx is not found, please create it and fill with test data");
    exit();

balance_sheet = wb['balance'];
expected_result_column = ascii_uppercase[len(balance_sheet['1'])]; # expected_result header default to last place
for i in ascii_uppercase:  # to find expected_result header location
    if(balance_sheet[i+'1'].value == "expected_result"):
        expected_result_column = i;

if(balance_sheet[expected_result_column+"1"].value!="expected_result"):
    balance_sheet[expected_result_column+"1"].value = "expected_result";
headers=balance_sheet['1'];
doj_index = probation_index = current_date_index = deactivated_on_index = allotment_index = cycle_index = prorata_index = accrual_index = workingdays_index = None

for header in headers:     # to find the indexes of headers from the data excel
    if(header.value == 'doj'):
        doj_index = headers.index(header);
    elif(header.value == 'probation'):
        probation_index = headers.index(header);
    elif(header.value == 'current_date'):
        current_date_index = headers.index(header);
    elif(header.value == 'deactivated_on'):
        deactivated_on_index = headers.index(header);
    elif(header.value == 'allotment'):
        allotment_index = headers.index(header);
    elif(header.value == 'cycle'):
        cycle_index = headers.index(header);
    elif(header.value == 'prorata'):
        prorata_index = headers.index(header);
    elif(header.value == 'accrual'):
        accrual_index = headers.index(header);
    elif(header.value == 'workingdays'):
        workingdays_index = headers.index(header);
    elif(header.value == 'expected_result'):
        result_index = headers.index(header);

for row_num in range(2,len(balance_sheet['A'])+1):  # To run the test for the rows having test data
    row = balance_sheet[str(row_num)];
    try:
        doj = row[doj_index].value if row[doj_index].value is not None else "";
        doj=str(doj).split(' ')[0];
    except:
        doj = "";
    try:
        probation = row[probation_index].value if row[probation_index].value is not None else 0;
    except:
        probation = 0;
    try:
        current_date = row[current_date_index].value if row[current_date_index].value is not None else "";
        current_date=str(current_date).split(' ')[0];
    except:
        current_date = "";
    try:
        deactivated_on = row[deactivated_on_index].value if row[deactivated_on_index].value is not None else "";
        deactivated_on=str(deactivated_on).split(' ')[0];
    except:
        deactivated_on = "";
    try:
        allotment = row[allotment_index].value if row[allotment_index].value is not None else 12;
    except:
        allotment = 12;
    try:
        cycle = row[cycle_index].value if row[cycle_index].value is not None else 1;
    except:
        cycle = 1;
    try:
        prorata = row[prorata_index].value if row[prorata_index].value is not None else "No";
    except:
        prorata = "No";
    try:
        accrual = row[accrual_index].value if row[accrual_index].value is not None else "No";
    except:
        accrual = "No";
    try:
        workingdays = row[workingdays_index].value if row[workingdays_index].value is not None else "No";
    except:
        workingdays = "No";
    result = bal.GetBalance(doj=doj, probation=probation, current_date=current_date, deactivated_on=deactivated_on, allotment=allotment, cycle=cycle, prorata=prorata, accrual=accrual, workingdays=workingdays);
    balance_sheet[expected_result_column+str(row_num)].value = result;
    try:
        wb.save('balance.xlsx');
    except PermissionError:
        print("Please close the data excel if it is open ");
        wb.close();
        exit();
    print(f"DOJ:{doj}, Probation:{probation}, current_date:{current_date}, deactivated_on:{deactivated_on}, allotment:{allotment}, cycle:{cycle}, Pro-Rata:{prorata}, Accrual:{accrual} ", f"Workingdays:{workingdays} " if workingdays != "No" else "", " ----> ",result);
    
