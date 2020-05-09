from selenium import webdriver
import os
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import requests
import time
url="https://automation6.qa.darwinbox.io"

# payload = f"UserLogin%5Busername%5D=hhggv&UserLogin%5Bpassword%5D=jhbjhvjv&UserLogin%5Bredirectpage%5D=dashboard&login-submit="
# with requests.session() as s:     #getting sessionid
#     s.post(url, data=payload)
#     sessionid = s.cookies.get('PHPSESSID')
#     print(sessionid)
#     print(s.headers.get('origin'))
#     r = requests.get(url,data=payload)
#     # print(r.text)
driver = webdriver.Chrome(ChromeDriverManager().install())   # installing a new web driver
driver.get(url)
actions = ActionChains(driver)
user_login_id = "automation6dotted"
user_pwd = "Dbox@123"
username = driver.find_element(By.ID, "UserLogin_username")
username.send_keys(user_login_id)
password = driver.find_element(By.ID, "UserLogin_password")
password.send_keys(user_pwd)
login_btn = driver.find_element(By.ID, "login-submit")
login_btn.click()
driver.get(url+"/dashboard/changeAccess")
driver.get(url+"/settings/leaves/create")

cycle=["Mar","Apr","Jul"]
leave_name=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

for eachcycle in cycle:
    for eachleave_name in leave_name:
        driver.find_element(By.ID, "dept_grp_company").send_keys("Ten")
        driver.find_element(By.ID, "Leaves_name").send_keys(eachcycle+"_"+eachleave_name+"_MA")
        driver.find_element(By.ID, "Leaves_yearly_endowment").send_keys("12")
        if eachcycle == "Jan":
            driver.find_element(By.ID, "Leaves_p4_carry_over_time").send_keys("Cal")
        elif eachcycle == "Apr":
            driver.find_element(By.ID, "Leaves_p4_carry_over_time").send_keys("Fin")
        else:
            driver.find_element(By.ID, "Leaves_p4_carry_over_time").send_keys("Cus")
            driver.find_element(By.ID, "Leaves_p4_custom_month").send_keys(eachcycle)


        # driver.find_element_by_id("Leaves_push_leaves_to_admin").click()

        # element = driver.find_element_by_css('div[class*="loadingWhiteBox"]') driver.execute_script("arguments[0].click();", element)
        # driver.implicitly_wait(10)
        # ActionChains(driver).move_to_element(button).click(button).perform()   
    
        #Multiple Allotment
        ma_checkbox = driver.find_element_by_xpath('//*[@id="use_multiple_allotment"]')
        actions.move_to_element(ma_checkbox).perform()
        ma_checkbox.click()
        driver.find_element_by_xpath('//*[@id="add_more_restriction_fields"]').click()
        driver.find_element_by_xpath('//*[@id="add_more_restriction_fields"]').click()
        fulltime = driver.find_element_by_xpath('//*[@id="Leaves_multiple_allotment_restriction_0_restriction_chosen"]/ul/li/input')
        driver.implicitly_wait(10)
        fulltime.send_keys(" Full Time")
        fulltime.send_keys(Keys.ENTER)
        fulltime_val = driver.find_element_by_xpath('//*[@id="Leaves_multiple_allotment_restriction_0_maximumLeaves"]')
        fulltime_val.send_keys("36")
        parttime = driver.find_element_by_xpath('//*[@id="Leaves_multiple_allotment_restriction_1_restriction_chosen"]/ul/li/input')
        parttime.click()
        driver.implicitly_wait(10)
        parttime.send_keys(" Part Time")
        parttime.send_keys(Keys.ENTER)
        parttime_val = driver.find_element_by_xpath('//*[@id="Leaves_multiple_allotment_restriction_1_maximumLeaves"]')
        parttime_val.send_keys("24")
        contract = driver.find_element_by_xpath('//*[@id="Leaves_multiple_allotment_restriction_2_restriction_chosen"]/ul/li/input')
        contract.click()
        driver.implicitly_wait(10)
        contract.send_keys(" Contract")
        contract.send_keys(Keys.ENTER)
        contract_val = driver.find_element_by_xpath('//*[@id="Leaves_multiple_allotment_restriction_2_maximumLeaves"]')
        contract_val.send_keys("12")

        # CarryForward
        cfwd_dropdown = driver.find_element_by_xpath('//*[@id="leavePolicyAccordion"]/div[5]/div/div[1]/div/a')
        actions.move_to_element(cfwd_dropdown).perform()
        cfwd_dropdown.click()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('/html/body/div[2]/div/section/div/div[4]/div[3]/div/div[5]/div/div[2]/div/div[1]/div/div[1]/div[1]/input').click()
        driver.implicitly_wait(10)
        driver.find_element(By.ID, "LeavePolicy_UnusedCarryover_status").click()
        driver.find_element_by_xpath('/html/body/div[2]/div/section/div/div[4]/div[3]/div/div[5]/div/div[2]/div/div[4]/div/div/div[1]/div/input').click()
        driver.find_element_by_xpath('/html/body/div[2]/div/section/div/div[4]/div[3]/div/div[5]/div/div[2]/div/div[4]/div/div/div[2]/select').send_keys(eachleave_name)
        # SAVE

        # driver.execute_script("window.scrollTo(0, 0)")
        save_button = driver.find_element_by_id('leave_policy_create_btn')
        actions.move_to_element(save_button).perform()
        save_button.click()
        exit()