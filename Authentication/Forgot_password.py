# Verify that the user is able to forgot the password

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

btn_element = driver.find_element(By.CSS_SELECTOR,'a[href="/login"]')
btn_element.click()

forgot_btn = driver.find_element(By.CSS_SELECTOR,'a[href="/forgot-password"]')
forgot_btn.click()
wait = WebDriverWait(driver, 10)

driver.find_element(By.CLASS_NAME,"form-control").send_keys("3334334345")

btn_element1 = driver.find_element(By.CSS_SELECTOR,'button[type="submit"]')
btn_element1.click()

time.sleep(5)

# get the current URL of the page
current_url_reset_password_otp = driver.current_url

if "reset-password-otp" in current_url_reset_password_otp:
    # print("Phone number successfully added and redirected to the OTP page")

    #for otp
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "otpInput")))
    for i, otp_input in enumerate(element):
        otp_input.send_keys(str(i+1))

    btn_element = driver.find_element(By.CSS_SELECTOR,'button[type="submit"]')
    btn_element.click()

    time.sleep(6)

    current_url_reset_password = driver.current_url
    if "reset-password" in current_url_reset_password:
        # print("OTP added successfully and redirected to the reset password page")

        # password
        password_input = wait.until(EC.presence_of_element_located((By.ID, "outlined-adornment-password")))
        password_input.send_keys("Sadiqkhang@1234")

        # confirm password
        confirm_pass_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[placeholder="Confirm Password"]')))
        confirm_pass_input.send_keys('Sadiqkhang@1234')

        password_value = password_input.get_attribute("value")
        confirm_pass_value = confirm_pass_input.get_attribute("value")
        if password_value == confirm_pass_value:
            # print('Password and confirm password matched')
            btn_element3 = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
            btn_element3.click()

            time.sleep(5)
            current_url_login = driver.current_url
            if "login" in current_url_login:
                print("Reset password test  passed")
            else:
                driver.quit()
                raise SystemExit("Reset password test failed")
        else:
            driver.quit()
            raise SystemExit("Password and confirm password do not match")
    else:
        driver.quit()
        raise SystemExit("OTP not added or was not redirected to the password page")
else:
    driver.quit()
    raise SystemExit("Phone number not added or was not redirected to the OTP page")