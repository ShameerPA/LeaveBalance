def BOM(cstart, current_date, midjoining):
    monthscount = (current_date.year - cstart.year)*12 + (current_date.month - cstart.month) + 1;
    if(cstart.day>=15):
        monthscount -= midjoining;
    return_value = monthscount if monthscount > 0 else 0;
    #print(f"\n\n cycle Start = {cstart} \n current_date {current_date} \n months count = {monthscount}");
    return return_value;

def EOM(cstart, current_date, midjoining):
    monthscount = (current_date.year - cstart.year)*12 + (current_date.month - cstart.month) + 1;
    monthscount -= 1;
    if(cstart.day>=15):
        monthscount -= midjoining;
    return_value = monthscount if monthscount > 0 else 0;
    return return_value;

def BOQ(cstart, current_date, midjoining):
    monthscount = (current_date.year - cstart.year)*12 + (current_date.month - cstart.month) + 1;
    if(monthscount >= 0 and monthscount <= 3):
        monthscount = 3
    elif(monthscount > 3 and monthscount <= 6 ):
        monthscount = 6
    elif(monthscount > 6 and monthscount <= 9 ):
        monthscount = 9
    elif(monthscount > 9 and monthscount <= 12 ):
        monthscount = 12
    if(cstart.day>=15):
        monthscount -= midjoining;
    return_value = monthscount if monthscount > 0 else 0;
    return return_value;

def EOQ(cstart, current_date, midjoining):
    monthscount = (current_date.year - cstart.year)*12 + (current_date.month - cstart.month) + 1;
    if(monthscount >= 0 and monthscount <= 3):
        monthscount = 0
    elif(monthscount > 3 and monthscount <= 6 ):
        monthscount = 3
    elif(monthscount > 6 and monthscount <= 9 ):
        monthscount = 6
    elif(monthscount > 9 and monthscount <= 12 ):
        monthscount = 9
    if(cstart.day>=15):
        monthscount -= midjoining;
    return_value = monthscount if monthscount > 0 else 0;
    return return_value;

def BiA(cstart, current_date, midjoining):
    monthscount = (current_date.year - cstart.year)*12 + (current_date.month - cstart.month) + 1;
    if(monthscount >= 0 and monthscount <= 6):
        monthscount = 6
    elif(monthscount > 6 and monthscount <= 12 ):
        monthscount = 12
    if(cstart.day>=15):
        monthscount -= midjoining;
    return_value = monthscount if monthscount > 0 else 0;
    return return_value;


'''
python
import GetBalance as Bal
Bal.GetBalance(doj = "2020-01-01", allotment = 12, cycle = 1, prorata = "No", accrual = "BOQ", workingdays = "No", probation = 0, current_date = "2020-04-01")

'''




