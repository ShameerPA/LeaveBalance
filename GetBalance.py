#This is a leave balance method:
#allotment(Int) - Whole Number
#cycle(int) - 1:"Jan", 2:"Feb", 3:"Mar", 4:"Apr", 5:"May", 6:"Jun", 7:"Jul", 8:"Aug", 9:"Sep", 10:"Oct", 11:"Nov", 12:"Dec"
#proRata(Str) - "No"(Default), "Joining_None", "Joining_Half", "Joining_Full", "Probation_None", "Probation_Half", "Probation_Full"
#accrual(Str) - "No"(Default), "BOM", "EOM", "BOQ", "EOQ", "BiA"
#workingDays - "No"(Default), "Yes_No", "Yes_EOY"
#probation - 0(Default), Any +ve integer, "Probation"
#current_date = Today(Default)

import datetime
import balance as balances
class GetBalance():

    def __str__(self):
        return "This is for getting balance/Deactivated_balance based on ProRata and Accrual combinations"
    def GetBalance(self, **kwargs):
        if(len(kwargs) == 0):
            print('''
    please call in the below format:

    Bal.GetBalance(doj = "2020-01-01", allotment = 12, cycle = 1, prorata = "No", accrual = "BOQ", workingdays = "No", probation = 0, current_date = "2020-04-01", deactivated_on = "2020-04-01")

    default values are

    doj = "1970-01-01", allotment = 12, cycle = 1, prorata = "No", accrual = "No", workingdays = "No", probation = 0, current_date = date_now 


    ''');

        doj = kwargs['doj'] if 'doj' in kwargs and kwargs['doj']!="" else "1970-01-01";
        allotment = kwargs['allotment'] if 'allotment' in kwargs and kwargs['allotment']!="" else 12
        cycle = kwargs['cycle'] if 'cycle' in kwargs and kwargs['cycle']!="" else 1;
        prorata = kwargs['prorata'] if 'prorata' in kwargs and kwargs['prorata']!="" else 'No';
        accrual = kwargs['accrual'] if 'accrual' in kwargs and kwargs['accrual']!="" else 'No';
        workingdays = kwargs['workingdays'] if 'workingdays' in kwargs and kwargs['workingdays']!="" else 'No';
        probation = kwargs['probation'] if 'probation' in kwargs and kwargs['probation']!="" else 0;
        if('current_date' in kwargs):
            if(kwargs['current_date']==""):
                current_date = datetime.date.today();
            else:
                try:
                    current_date = datetime.date.fromisoformat(kwargs['current_date']);
                except ValueError:
                    current_date = datetime.date.today();
                    current_date = datetime.date.fromisoformat(kwargs['current_date']);
                    print("PLease use yyyy-mm-dd  format for dates");
        else:
            current_date = datetime.date.today();
        current_date_spare = current_date;
        deactivated_on = kwargs['deactivated_on'] if 'deactivated_on' in kwargs and kwargs['deactivated_on']!="" else "9999-12-31";
        mid_joining = 0 if prorata == "joining_full" or prorata.lower() == "probation_full" else 0.5 if prorata.lower() == "joining_half" or prorata.lower()=="probation_half" else 1
        monthly = allotment/12;
        doj="1970-01-01" if doj == "" else doj;
        try:
            doj=datetime.date.fromisoformat(doj);
        except ValueError:
            doj=datetime.date.fromisoformat("1970-01-01");
            print("PLease use yyyy-mm-dd  format for dates");
        deactivated_on = "9999-12-31" if deactivated_on == "" else deactivated_on;
        try:
            deactivated_on = datetime.date.fromisoformat(deactivated_on);
        except ValueError:
            deactivated_on = datetime.date.fromisoformat("9999-12-31");
            print("PLease use yyyy-mm-dd  format for dates");
        if(current_date > deactivated_on):
            current_date = deactivated_on;
            accrual = "BOM";
                
        #Find Cycle_Start_Date and Cycle_End_Date
        if(current_date.month >= cycle):
            cycle_start_date = datetime.date(current_date.year, cycle, 1)
            cycle_end_date = datetime.date(current_date.year + 1, cycle, 1) - datetime.timedelta(days=1)
        else:
            cycle_start_date = datetime.date(current_date.year - 1, cycle, 1)
            cycle_end_date = datetime.date(current_date.year, cycle, 1) - datetime.timedelta(days=1)

        if(probation >=0):
            probation_end_date = doj + datetime.timedelta(days=probation);

        #Find DOJ is <= Cycle_Start_Date ? From = Cycle_Start_Date : From = DOJ ;
        if(doj>=cycle_start_date):
            cstart = doj;
        else:
            cstart = cycle_start_date;
        if(probation_end_date>=cycle_start_date):
            pcstart = probation_end_date;
        elif(doj>=cycle_start_date):
            pcstart = doj;
        else:
            pcstart = cycle_start_date

        #Pro Rata Joining_None
        if(prorata.lower() == 'joining_none'):
            if(accrual == 'BOM'):
                monthscount = 0 if (cstart>current_date) else balances.BOM(cstart, current_date, mid_joining);
            elif(accrual == 'EOM'):
                monthscount = 0 if (cstart>current_date) else balances.EOM(cstart, current_date, mid_joining);
            elif(accrual == 'BOQ'):
                monthscount = 0 if (cstart>current_date) else balances.BOQ(cstart, current_date, mid_joining);
            elif(accrual == 'EOQ'):
                monthscount = 0 if (cstart>current_date) else balances.EOQ(cstart, current_date, mid_joining);
            elif(accrual == 'BiA'):
                monthscount = 0 if (cstart>current_date) else balances.BiA(cstart, current_date, mid_joining);
            else:
                monthscount = balances.BOM(cstart, cycle_end_date, mid_joining);

        #Pro Rata Joining_Half
        elif(prorata.lower() == 'joining_half'):
            if(accrual == 'BOM'):
                monthscount = 0 if (cstart>current_date) else balances.BOM(cstart, current_date, mid_joining);
            elif(accrual == 'EOM'):
                monthscount = 0 if (cstart>current_date) else balances.EOM(cstart, current_date, mid_joining);
            elif(accrual == 'BOQ'):
                monthscount = 0 if (cstart>current_date) else balances.BOQ(cstart, current_date, mid_joining);
            elif(accrual == 'EOQ'):
                monthscount = 0 if (cstart>current_date) else balances.EOQ(cstart, current_date, mid_joining);
            elif(accrual == 'BiA'):
                monthscount = 0 if (cstart>current_date) else balances.BiA(cstart, current_date, mid_joining);
            else:
                monthscount = balances.BOM(cstart, cycle_end_date, mid_joining);

        #Pro Rata Joining_Full
        elif(prorata.lower() == 'joining_full'):
            if(accrual == 'BOM'):
                monthscount = 0 if (cstart>current_date) else balances.BOM(cstart, current_date, mid_joining);
            elif(accrual == 'EOM'):
                monthscount = 0 if (cstart>current_date) else balances.EOM(cstart, current_date, mid_joining);
            elif(accrual == 'BOQ'):
                monthscount = 0 if (cstart>current_date) else balances.BOQ(cstart, current_date, mid_joining);
            elif(accrual == 'EOQ'):
                monthscount = 0 if (cstart>current_date) else balances.EOQ(cstart, current_date, mid_joining);
            elif(accrual == 'BiA'):
                monthscount = 0 if (cstart>current_date) else balances.BiA(cstart, current_date, mid_joining);
            else:
                monthscount = balances.BOM(cstart, cycle_end_date, mid_joining);

        #Pro Rata Probation_None
        elif(prorata.lower() == 'probation_none'):
            if(accrual == 'BOM'):
                monthscount = 0 if (pcstart>current_date) else balances.BOM(pcstart, current_date, mid_joining);
            elif(accrual == 'EOM'):
                monthscount = 0 if (pcstart>current_date) else balances.EOM(pcstart, current_date, mid_joining);
            elif(accrual == 'BOQ'):
                monthscount = 0 if (pcstart>current_date) else balances.BOQ(pcstart, current_date, mid_joining);
            elif(accrual == 'EOQ'):
                monthscount = 0 if (pcstart>current_date) else balances.EOQ(pcstart, current_date, mid_joining);
            elif(accrual == 'BiA'):
                monthscount = 0 if (pcstart>current_date) else balances.BiA(pcstart, current_date, mid_joining);
            else:
                monthscount = balances.BOM(pcstart, cycle_end_date, mid_joining);

        #Pro Rata Probation_Half
        elif(prorata.lower() == 'probation_half'):
            if(accrual == 'BOM'):
                monthscount = 0 if (pcstart>current_date) else balances.BOM(pcstart, current_date, mid_joining);
            elif(accrual == 'EOM'):
                monthscount = 0 if (pcstart>current_date) else balances.EOM(pcstart, current_date, mid_joining);
            elif(accrual == 'BOQ'):
                monthscount = 0 if (pcstart>current_date) else balances.BOQ(pcstart, current_date, mid_joining);
            elif(accrual == 'EOQ'):
                monthscount = 0 if (pcstart>current_date) else balances.EOQ(pcstart, current_date, mid_joining);
            elif(accrual == 'BiA'):
                monthscount = 0 if (pcstart>current_date) else balances.BiA(pcstart, current_date, mid_joining);
            else:
                monthscount = balances.BOM(pcstart, cycle_end_date, mid_joining);

        #Pro Rata Probation_Full
        elif(prorata.lower() == 'probation_full'):
            if(accrual == 'BOM'):
                monthscount = 0 if (pcstart>current_date) else balances.BOM(pcstart, current_date, 0);
            elif(accrual == 'EOM'):
                monthscount = 0 if (pcstart>current_date) else balances.EOM(pcstart, current_date, 0);
            elif(accrual == 'BOQ'):
                monthscount = 0 if (pcstart>current_date) else balances.BOQ(pcstart, current_date, 0);
            elif(accrual == 'EOQ'):
                monthscount = 0 if (pcstart>current_date) else balances.EOQ(pcstart, current_date, 0);
            elif(accrual == 'BiA'):
                monthscount = 0 if (pcstart>current_date) else balances.BiA(pcstart, current_date, 0);
            else:
                monthscount = balances.BOM(pcstart, cycle_end_date, 0);

        #Pro Rata NO
        else:
            if(accrual == 'BOM'):
                monthscount = balances.BOM(cycle_start_date, current_date, mid_joining);
            elif(accrual == 'EOM'):
                monthscount = balances.EOM(cycle_start_date, current_date, mid_joining);
            elif(accrual == 'BOQ'):
                monthscount = balances.BOQ(cycle_start_date, current_date, mid_joining);
            elif(accrual == 'EOQ'):
                monthscount = balances.EOQ(cycle_start_date, current_date, mid_joining);
            elif(accrual == 'BiA'):
                monthscount = balances.BiA(cycle_start_date, current_date, mid_joining);
            else:
                monthscount = balances.BOM(cycle_start_date, cycle_end_date, mid_joining);

        if(current_date_spare > deactivated_on):
            if(deactivated_on.day < 15):
                monthscount = monthscount - mid_joining;
        calculated_balance = monthscount*monthly if monthscount >= 0 else 0
        return calculated_balance;
