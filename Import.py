from openpyxl import load_workbook
import datetime
import GetBalance as Balance
import CreateLeavePolicy
ascii_uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
bal=Balance.GetBalance()
try:
    wb = load_workbook("Sam.xlsx")
except FileNotFoundError:
    print("balance.xlsx is not found, please create it and fill with test data")
    exit()
balance_sheet = wb['Sam']
count = 1
for i in range(1,51,1):
    date = datetime.date.fromisoformat("2020-09-01")
    while date<datetime.date.fromisoformat("2020-10-02"):
        balance_sheet["A"+str(count)].value = "15281employee" + str(i)
        balance_sheet["B"+str(count)].value = date
        print("15281employee" + str(i) + "\t" + str(date))
        date += datetime.timedelta(days=1)
        count += 1
wb.save("Sam.xlsx")