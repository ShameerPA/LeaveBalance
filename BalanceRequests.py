from selenium import webdriver
import os
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
url="https://automation.qa.darwinbox.io"
driver = webdriver.Chrome(ChromeDriverManager().install())   # installing a new web driver
driver.get(url);
user_login_id = "automation@yopmail.com"
user_pwd = "0987654321";
username = driver.find_element(By.ID, "UserLogin_username");
username.send_keys(user_login_id);
password = driver.find_element(By.ID, "UserLogin_password");
password.send_keys(user_pwd);
login_btn = driver.find_element(By.ID, "login-submit");
login_btn.click();
driver.get(url+"/dashboard/changeAccess");
driver.get(url+"/settings/leaves")
