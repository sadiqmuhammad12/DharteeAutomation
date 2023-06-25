# Verify that the user is redirected to the packages page
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")

driver = webdriver.Chrome(service=serv_obj)

driver.get("https://dev.dhartee.pk/")
driver.maximize_window()
Packages_link = driver.find_element(By.XPATH, "//p[text()='Packages']")
Packages_link.click()

time.sleep(4)
if 'packages' in driver.current_url:
    print('User is redirected to the packages page')
else:
    print("User does not redirected to the packages page")
# close the web driver instance
driver.quit()


