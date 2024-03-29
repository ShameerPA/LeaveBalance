from selenium import webdriver
import os
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from openpyxl import load_workbook
import time

import requests
import time
class CreatePolicy():
    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password

    def login(self, driver):  # Login
        driver.get(self.url)
        driver.find_element(By.ID, "UserLogin_username").send_keys(self.username)
        driver.find_element(By.ID, "UserLogin_password").send_keys(self.password)
        driver.find_element(By.ID, "login-submit").click()
        return True

    def change_access(self,driver):
        driver.get(self.url+'/dashboard/changeAccess')

    def OpenChromeDriver():  # installing a new web driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        return driver



    def create(self,driver,leave_data):
        actions = ActionChains(driver)
        if leave_data['group_company']!="":     #Group Company
            driver.find_element(By.ID, "dept_grp_company").send_keys(leave_data['group_company'][:3])
        if leave_data['leave_name']=="":        #Leave Name
            return "leave_type not found"
        else:
            driver.find_element(By.ID, "Leaves_name").send_keys(leave_data['leave_name'])
        if leave_data['hourly'].lower()=="yes":     #Hourly
            driver.find_element(By.XPATH, '/html/body/div[2]/div/section/div/div/div[1]/form/div[1]/div[5]/div[5]/div/input[2]').click
        now = datetime.today().strftime(r'%d-%m-%y, %H:%M:%S')
        if leave_data['description']=="" or leave_data['description']== None:       #Description
            driver.find_element(By.ID, "Leaves_description").send_keys(f'{leave_data}\nCreated on {now}\n by automation')
        else:
            driver.find_element(By.ID, "Leaves_description").send_keys(leave_data['description']+'\n\n created by automation on '+now)
        if leave_data['annual'] != "":          #Annual Allotment
            driver.find_element(By.ID, "Leaves_yearly_endowment").send_keys(leave_data['annual'])
        else:
            driver.find_element(By.ID, "Leaves_yearly_endowment").send_keys("12")
        if leave_data['cycle'].lower() == "jan":
            pass
        elif leave_data['cycle'].lower() == "apr":        #Cycle
            driver.find_element(By.ID, "Leaves_p4_carry_over_time").send_keys("Fin")
        else:
            driver.find_element(By.ID, "Leaves_p4_carry_over_time").send_keys("Cus")
            driver.find_element(By.ID, "Leaves_p4_custom_month").send_keys(leave_data['cycle'])

#        if(leave_data['restriction'].lower()!="no" or leave_data['restriction'].lower()==""):   #Restriction
#            restriction = driver.find_element_by_xpath('/html/body/div[2]/div/section/form/div/div[1]/div/div[5]/div[8]/div[2]/div/ul')
#            restriction.send_keys(leave_data['restriction'])
#            restriction.send_keys(Keys.ENTER)
#            time.sleep(1)
#            time.sleep(100)
        time.sleep(1)
        pushadmin = driver.find_element_by_xpath('/html/body/div[2]/div/section/form/div/div[1]/div/div[5]/div[13]/div/input')   #Push to Admin Always checked.
        actions.move_to_element(pushadmin).perform()
        pushadmin.click()
                                #Retention_Of_TransferBalance
        if leave_data['Retention_Of_TransferBalance'].lower() != '' and leave_data['Retention_Of_TransferBalance'].lower() != 'No':
            driver.find_element_by_xpath('/html/body/div[2]/div/section/form/div/div[1]/div/div[5]/div[14]/div/input').click()

                            #Gender Applicability
        Gender_Applicability = leave_data['Gender_Applicability'].lower()
        if Gender_Applicability != 'no' and Gender_Applicability != '':
            value = driver.find_element_by_xpath('/html/body/div[2]/div/section/div/div[1]/form/div/div[6]/div[6]/div/a/span').send_keys(leave_data['Gender_Applicability'])
            value.click()

                            #Leave Probation
        Leave_Probation = str(leave_data['Leave_Probation']).lower()
        if Leave_Probation != '' and Leave_Probation != '0' :
            if Leave_Probation == 'employee':
                driver.find_element_by_xpath('/html/body/div[2]/div/section/form/div/div[1]/div/div[6]/div[16]/div[2]/input').click()
            else:
                value = driver.find_element_by_xpath('/html/body/div[2]/div/section/form/div/div[1]/div/div[6]/div[17]/input')
                value.clear()
                value.send_keys(leave_data['Leave_Probation'])

                                #Tenure
        if leave_data['Tenure'].lower() != '' and leave_data['Tenure'].lower() != 'no':
            value = driver.find_element_by_xpath('/html/body/div[2]/div/section/form/div/div[4]/div[3]/div/div[3]/div/div[1]/div/a')
            actions.move_to_element(value).perform()
            value.click()
            time.sleep(1)
            driver.find_element_by_xpath('/html/body/div[2]/div/section/form/div/div[4]/div[3]/div/div[3]/div/div[2]/div/div/div/div[1]/div[1]/input').click()
            driver.find_element_by_xpath('/html/body/div[2]/div/section/form/div/div[4]/div[3]/div/div[3]/div/div[2]/div/div/div/div[3]/div[2]/div/table/tbody/tr[1]/td[2]/select').send_keys('2')
            driver.find_element_by_xpath('/html/body/div[2]/div/section/form/div/div[4]/div[3]/div/div[3]/div/div[2]/div/div/div/div[3]/div[2]/div/table/tbody/tr[1]/td[3]/input').send_keys('24')
            driver.find_element_by_xpath('/html/body/div[2]/div/section/form/div/div[4]/div[3]/div/div[3]/div/div[2]/div/div/div/div[3]/div[2]/div/div/a').click()
            driver.find_element_by_xpath('/html/body/div[2]/div/section/form/div/div[4]/div[3]/div/div[3]/div/div[2]/div/div/div/div[3]/div[2]/div/table/tbody/tr[2]/td[1]/select').send_keys('2')
            driver.find_element_by_xpath('/html/body/div[2]/div/section/form/div/div[4]/div[3]/div/div[3]/div/div[2]/div/div/div/div[3]/div[2]/div/table/tbody/tr[2]/td[2]/select').send_keys('3')
            driver.find_element_by_xpath('/html/body/div[2]/div/section/form/div/div[4]/div[3]/div/div[3]/div/div[2]/div/div/div/div[3]/div[2]/div/table/tbody/tr[2]/td[3]/input').send_keys('36')

        if leave_data['multiple_allotment'].lower() == 'yes':                   #Multiple Allotment
            ma_checkbox = driver.find_element_by_xpath('/html/body/div[2]/div/section/form/div/div[1]/div/div[10]/div[1]/input')
            actions.move_to_element(ma_checkbox).perform()
            ma_checkbox.click()
            driver.implicitly_wait(10)
            value = driver.find_element_by_xpath('/html/body/div[2]/div/section/form/div/div[1]/div/div[10]/div[2]/div/a')
            value.click()
            driver.implicitly_wait(10)
            value.click()
            driver.implicitly_wait(10)
            fulltime = driver.find_element_by_xpath('/html/body/div[2]/div/section/form/div/div[1]/div/div[10]/div[2]/table/tbody/tr[1]/td[2]/div/ul/li/input')
            fulltime.click()
            fulltime.send_keys("Full Time")
            fulltime.send_keys(Keys.ENTER)
            fulltime_val = driver.find_element_by_xpath('/html/body/div[2]/div/section/form/div/div[1]/div/div[10]/div[2]/table/tbody/tr[1]/td[3]/input')
            fulltime_val.send_keys("36")
            parttime = driver.find_element_by_xpath('/html/body/div[2]/div/section/form/div/div[1]/div/div[10]/div[2]/table/tbody/tr[2]/td[2]/div/ul/li/input')
            parttime.click()
            driver.implicitly_wait(20)
            parttime.send_keys(" Part Time")
            parttime.send_keys(Keys.ENTER)
            parttime_val = driver.find_element_by_xpath('/html/body/div[2]/div/section/form/div/div[1]/div/div[10]/div[2]/table/tbody/tr[2]/td[3]/input')
            parttime_val.send_keys("24")
            contract = driver.find_element_by_xpath('/html/body/div[2]/div/section/form/div/div[1]/div/div[10]/div[2]/table/tbody/tr[3]/td[2]/div/ul/li/input')
            contract.click()
            driver.implicitly_wait(20)
            contract.send_keys(" Contract")
            contract.send_keys(Keys.ENTER)
            contract_val = driver.find_element_by_xpath('/html/body/div[2]/div/section/form/div/div[1]/div/div[10]/div[2]/table/tbody/tr[3]/td[3]/input')
            contract_val.send_keys("12")
        if leave_data['prorata'].lower() != 'no' and leave_data['prorata'].lower() != "":           #Prorata
            prorata_dropdown = driver.find_element_by_xpath('//*[@id="leavePolicyAccordion"]/div/div[1]/div[1]/div/a')
            actions.move_to_element(prorata_dropdown).perform()
            prorata_dropdown.click()
            time.sleep(1)
            driver.find_element_by_xpath('/html/body/div[2]/div/section/form/div/div[4]/div[3]/div/div[1]/div/div[2]/div/div[1]/div/div[1]/div[1]/input').click()
            if leave_data['prorata'].lower() == 'joining_half':
                driver.find_element_by_xpath('/html/body/div[2]/div/section/form/div/div[4]/div[3]/div/div[1]/div/div[2]/div/div[2]/div/div/div[2]/div[1]/input').click()
            elif leave_data['prorata'].lower() == 'joining_full':
                driver.find_element_by_xpath('/html/body/div[2]/div/section/form/div/div[4]/div[3]/div/div[1]/div/div[2]/div/div[2]/div/div/div[2]/div[2]/input').click()
            elif leave_data['prorata'].lower() == 'probation_none':
                driver.find_element_by_xpath('/html/body/div[2]/div/section/form/div/div[4]/div[3]/div/div[1]/div/div[2]/div/div[2]/div/div/div[1]/div[2]/input').click()
            elif leave_data['prorata'].lower() == 'probation_half':
                driver.find_element_by_xpath('/html/body/div[2]/div/section/form/div/div[4]/div[3]/div/div[1]/div/div[2]/div/div[2]/div/div/div[1]/div[2]/input').click()
                driver.find_element_by_xpath('/html/body/div[2]/div/section/form/div/div[4]/div[3]/div/div[1]/div/div[2]/div/div[2]/div/div/div[2]/div[1]/input').click()
            elif leave_data['prorata'].lower() == 'probation_full':
                driver.find_element_by_xpath('/html/body/div[2]/div/section/div/div[4]/div[3]/div/div[1]/div/div[2]/div/div[2]/div/div/div[1]/div[2]/input').click()
                driver.find_element_by_xpath('/html/body/div[2]/div/section/form/div/div[4]/div[3]/div/div[1]/div/div[2]/div/div[2]/div/div/div[2]/div[2]/input').click()

        if leave_data['accrual'].lower() != 'no' and leave_data['accrual'].lower() != '':           #accrual
            accrual_dropdown = driver.find_element_by_xpath('//*[@id="leavePolicyAccordion"]/div[2]/div/div[1]/div/a')
            actions.move_to_element(accrual_dropdown).perform()
            accrual_dropdown.click()
            time.sleep(1)
            driver.find_element_by_xpath('/html/body/div[2]/div/section/form/div/div[4]/div[3]/div/div[2]/div/div[2]/div/div/div/div[1]/div[1]/input').click()
            if leave_data['accrual'].lower() == 'eom':
                driver.find_element_by_xpath('/html/body/div[2]/div/section/form/div/div[4]/div[3]/div/div[2]/div/div[2]/div/div/div/div[5]/div[2]/input').click()
            elif leave_data['accrual'].lower() == 'boq':
                driver.find_element_by_xpath('/html/body/div[2]/div/section/form/div/div[4]/div[3]/div/div[2]/div/div[2]/div/div/div/div[3]/div[2]/input').click()
            elif leave_data['accrual'].lower() == 'eoq':
                driver.find_element_by_xpath('/html/body/div[2]/div/section/form/div/div[4]/div[3]/div/div[2]/div/div[2]/div/div/div/div[3]/div[2]/input').click()
                driver.find_element_by_xpath('/html/body/div[2]/div/section/form/div/div[4]/div[3]/div/div[2]/div/div[2]/div/div/div/div[4]/div[2]/input').click()
            elif leave_data['accrual'].lower() == 'bia':
                driver.find_element_by_xpath('/html/body/div[2]/div/section/form/div/div[4]/div[3]/div/div[2]/div/div[2]/div/div/div/div[3]/div[3]/input').click()
            if leave_data['workingdays'].lower() != '' and leave_data['workingdays'].lower() != 'no' :
                working = driver.find_element_by_xpath('/html/body/div[2]/div/section/form/div/div[4]/div[3]/div/div[2]/div/div[2]/div/div/div/div[3]/div[4]/div/input')
                actions.move_to_element(working).perform()
                working.click()
                driver.find_element_by_id('LeavePolicy_Accural_count_presents').click()
                driver.find_element_by_id('LeavePolicy_Accural_count_holiday').click()
                driver.find_element_by_id('LeavePolicy_Accural_count_leaves').click()
                driver.find_element_by_id('LeavePolicy_Accural_count_weeklyoff').click()
                driver.find_element_by_id('LeavePolicy_Accural_count_optional_holiday').click()
                driver.find_element_by_id('LeavePolicy_Accural_count_absent').click()
            if leave_data['workingdays'].lower() == 'eoy':
                driver.find_element_by_xpath('/html/body/div[2]/div/section/form/div/div[4]/div[3]/div/div[2]/div/div[2]/div/div/div/div[6]/div[2]/div/div/div/input').click()

        if leave_data['carry_forward'].lower() != "" and leave_data['carry_forward'].lower() != "no":           #Carry forward
            cfwd_dropdown = driver.find_element_by_xpath('//*[@id="leavePolicyAccordion"]/div[5]/div/div[1]/div/a')
            actions.move_to_element(cfwd_dropdown).perform()
            cfwd_dropdown.click()
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/div[2]/div/section/form/div/div[4]/div[3]/div/div[5]/div/div[2]/div/div[1]/div/div[1]/div[1]/input').click()
            driver.implicitly_wait(10)
            if leave_data['carry_forward'].lower() == "fixed" or leave_data['carry_forward'].lower() == 'percentage':
                driver.find_element_by_xpath('/html/body/div[2]/div/section/form/div/div[4]/div[3]/div/div[5]/div/div[2]/div/div[1]/div/div[3]/div[2]/input').click()
                driver.implicitly_wait(10)
                cfwd = driver.find_element_by_id('/html/body/div[2]/div/section/form/div/div[4]/div[3]/div/div[5]/div/div[2]/div/div[2]/div/div[1]/select')
                cfwd.send_keys(leave_data['carry_forward'][:4])
                cfwd.send_keys(Keys.ENTER)
                driver.find_element_by_id('LeavePolicy_UnusedCarryover_carry_forward_amount').send_keys(leave_data['carry_forward_amount'])
                if leave_data['remaining_carryforward'].lower() == 'encash':
                    driver.find_element_by_xpath('/html/body/div[2]/div/section/form/div/div[4]/div[3]/div/div[5]/div/div[2]/div/div[2]/div/div[2]/div[2]/input').click()
                if leave_data['carry_forward_lapse'].lower() != 'no' and leave_data['carry_forward_lapse'].lower() != '':       #Carry Forward Lapse
                    driver.find_element_by_xpath('/html/body/div[2]/div/section/form/div/div[4]/div[3]/div/div[5]/div/div[2]/div/div[4]/div/div/div[1]/div/input').click()
                    driver.implicitly_wait(10)
                    driver.find_element_by_id('LeavePolicy_UnusedCarryover_validaty_month').send_keys(leave_data['carry_forward_lapse'])
        save_button = driver.find_element_by_id('leave_policy_create_btn')
        actions.move_to_element(save_button).perform()
        save_button.click()
        if __name__ != "__main__":
            driver.get(url+"/settings/leaves/edit")
        return True

if __name__ == "__main__":
    try:
        wb = load_workbook("balance.xlsx")
    except FileNotFoundError:
        print("balance.xlsx is not found, please create it and fill with test data")
    configuration_sheet = wb['configuration']
    leave_policy_sheet = wb['leave_policy']
    url = configuration_sheet['A2'].value if configuration_sheet['A2'].value != '' and configuration_sheet['A2'].value != None else 'https://automation.qa.darwinbox.io'
    username = configuration_sheet['B2'].value if configuration_sheet['B2'].value != '' and configuration_sheet['B2'].value != None else 'automation@yopmail.com'
    password = configuration_sheet['C2'].value if configuration_sheet['C2'].value != '' and configuration_sheet['C2'].value != None else '0987654321'
    createObject = CreatePolicy(url,username,password)
    driver = CreatePolicy.OpenChromeDriver()
    createObject.login(driver)
    createObject.change_access(driver)
    driver.get(createObject.url+'/settings/leaves/create')
    print(url)
    leave_data = {'group_company':'', 'leave_name':'', 'hourly':'', 'description':'', 'annual':'','restriction':'no', 'cycle':'', 'multiple_allotment':'', 'prorata':'no', 'accrual':'no', 'carry_forward':'no', 'carry_forward_lapse':'no', 'Retention_Of_TransferBalance':'No','Tenure':'No', 'Gender_Applicability':'For All', 'Leave_Probation':'0', 'Halfday_Leave':'No', 'Count_Intervening':'No', 'Allow_Past':'No'}

    for row_num in range(2,len(leave_policy_sheet['A'])+1):
        leave_data = {'group_company':leave_policy_sheet['A'+str(row_num)].value, 'leave_name':leave_policy_sheet['B'+str(row_num)].value, 'hourly':leave_policy_sheet['C'+str(row_num)].value, 'description':leave_policy_sheet['D'+str(row_num)].value, 'annual':leave_policy_sheet['E'+str(row_num)].value,'restriction':leave_policy_sheet['F'+str(row_num)].value, 'cycle':leave_policy_sheet['G'+str(row_num)].value, 'multiple_allotment':leave_policy_sheet['H'+str(row_num)].value, 'prorata':leave_policy_sheet['I'+str(row_num)].value, 'accrual':leave_policy_sheet['J'+str(row_num)].value, 'workingdays':leave_policy_sheet['K'+str(row_num)].value,'carry_forward':leave_policy_sheet['L'+str(row_num)].value, 'carry_forward_amount':leave_policy_sheet['M'+str(row_num)].value,'remaining_carryforward':leave_policy_sheet['N'+str(row_num)].value,'carry_forward_lapse':leave_policy_sheet['O'+str(row_num)].value, 'Retention_Of_TransferBalance':leave_policy_sheet['P'+str(row_num)].value,'Tenure':leave_policy_sheet['Q'+str(row_num)].value, 'Gender_Applicability':leave_policy_sheet['R'+str(row_num)].value, 'Leave_Probation':leave_policy_sheet['S'+str(row_num)].value, 'Halfday_Leave':leave_policy_sheet['T'+str(row_num)].value, 'Count_Intervening':leave_policy_sheet['U'+str(row_num)].value, 'Allow_Past':leave_policy_sheet['V'+str(row_num)].value}
        print(row_num-1,end="")
        print(leave_data)
        status = createObject.create(driver, leave_data)
