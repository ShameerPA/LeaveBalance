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
user_login_id = "automation@yopmail.com"
user_pwd = "0987654321"
username = driver.find_element(By.ID, "UserLogin_username")
username.send_keys(user_login_id)
password = driver.find_element(By.ID, "UserLogin_password")
password.send_keys(user_pwd)
login_btn = driver.find_element(By.ID, "login-submit")
login_btn.click()
driver.get(url+"/dashboard/changeAccess")
driver.get(url+"/settings/leaves")
# This is the line added in Atom editor
