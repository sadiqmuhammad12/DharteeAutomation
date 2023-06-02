from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://dev.dhartee.pk/")
driver.find_element(By.CLASS_NAME,"MuiAvatar-circular").click()
driver.find_element(By.CLASS_NAME,"form-control").send_keys("4445676590")

btn_element = driver.find_element(By.CSS_SELECTOR,'button[type="submit"]')
btn_element.click()

time.sleep(5)

# get the current URL of the page
current_url = driver.current_url

if "verify_otp" in current_url:
    # print("Phone number successfully added and redirected to the OTP page")

    #for otp
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "otpInput")))
    for i, otp_input in enumerate(element):
        otp_input.send_keys(str(i+1))

    btn_element = driver.find_element(By.CSS_SELECTOR,'button[type="submit"]')
    btn_element.click()

    time.sleep(6)
    current_url_password = driver.current_url
    if "password" in current_url_password:
        # print("OTP added successfully and redirected to the password page")

        # password
        password_input = wait.until(EC.presence_of_element_located((By.ID, "outlined-adornment-password")))
        password_input.send_keys("Sadiqkhang@123")

        btn_element1 = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        btn_element1.click()

        time.sleep(6)

        current_url_profile_setting = driver.current_url
        if "profile-setting" in current_url_profile_setting:
            print("Sign up test passed")
        else:
            print("Sign up test failed")
            driver.quit()
    else:
        driver.quit()
        raise SystemExit("OTP not added or was not redirected to the password page")
else:
    # print("Phone number not added or was not redirected to the OTP page")
    driver.quit()
    raise SystemExit("Phone number not added or was not redirected to the OTP page")
