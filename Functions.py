from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
actions = ActionChains(driver)
url = "https://automation6.qa.darwinbox.io"
driver.get(url)
driver.get(url)
driver.find_element(By.ID, "UserLogin_username").send_keys('automation6dotted')
driver.find_element(By.ID, "UserLogin_password").send_keys('Dbox@123')
driver.find_element(By.ID, "login-submit").click()
driver.get(url+'/dashboard/changeAccess')
driver.get(url+'/settings/leaves/create')

prorata_dropdown = driver.find_element_by_xpath('//*[@id="leavePolicyAccordion"]/div/div[1]/div[1]/div/a')
actions.move_to_element(prorata_dropdown).perform()
time.sleep(1)
prorata_dropdown.click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="LeavePolicy_Prorated_status"]').click()
driver.find_element_by_xpath('/html/body/div[2]/div/section/div/div[4]/div[3]/div/div[1]/div/div[2]/div/div[2]/div/div/div[1]/div[2]/input').click()