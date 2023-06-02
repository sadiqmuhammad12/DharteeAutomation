# Verify that the user is redirects to the dashboard page

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://dev.dhartee.pk/")
driver.find_element(By.CLASS_NAME, "MuiAvatar-circular").click()

btn_element = driver.find_element(By.CSS_SELECTOR, 'a[href="/login"]')
btn_element.click()

wait = WebDriverWait(driver, 10)
driver.find_element(By.CLASS_NAME, "form-control").send_keys("3334334345")

driver.find_element(By.ID, 'outlined-adornment-password').send_keys("Sadiqkhang@1234")
btn_element1 = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
btn_element1.click()

time.sleep(6)

# get the current URL of the page
current_url = driver.current_url

# check if the expected text is in the URL
if "dashboard" in current_url:
    print("User is logged in and redirected to the dashboard page")
else:
    print("User login failed or was not redirected to the dashboard page")

# close the web driver instance
driver.quit()
