# Verify that the user is redirected to the profile-setting page
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from datetime import date
import time

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")

driver = webdriver.Chrome(service=serv_obj)

driver.get("https://dev.dhartee.pk/")
driver.maximize_window()

driver.find_element(By.CLASS_NAME, "MuiAvatar-circular").click()

btn_element = driver.find_element(By.CSS_SELECTOR, 'a[href="/login"]')
btn_element.click()

wait = WebDriverWait(driver, 10)
driver.find_element(By.CLASS_NAME, "form-control").send_keys("3334334345")

driver.find_element(By.ID, 'outlined-adornment-password').send_keys("Sadiqkhang@1234")
btn_element1 = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
btn_element1.click()

time.sleep(6)

# check if the expected text is in the URL
if "dashboard" in driver.current_url:
    # print("User is redirected to the dashboard page")
    profile_icon = driver.find_element(By.CLASS_NAME,'MuiAvatar-img')
    time.sleep(5)
    profile_icon.click()
    time.sleep(5)

    profile_link = driver.find_element(By.XPATH, "//a[text()='Profile']")
    profile_link.click()
    time.sleep(5)

    if 'profile-setting' in driver.current_url:
        print("User is redirected to the profile-setting page")
    else:
        print("User does not redirected to the profile-setting page")



else:
    print("User login failed or was not redirected to the dashboard page")

# close the web driver instance
driver.quit()


