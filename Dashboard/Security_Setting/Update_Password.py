# Verify that the user is able to update the password
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import time

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://dev.dhartee.pk/")
driver.find_element(By.CLASS_NAME, "MuiAvatar-circular").click()

btn_element = driver.find_element(By.CSS_SELECTOR, 'a[href="/login"]')
btn_element.click()

wait = WebDriverWait(driver, 10)
driver.find_element(By.CLASS_NAME, "form-control").send_keys("3334334345")

driver.find_element(By.ID, 'outlined-adornment-password').send_keys("Sadiqkhang@123")
btn_element1 = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
btn_element1.click()

time.sleep(6)

# get the current URL of the page
current_url = driver.current_url

# check if the expected text is in the URL
if "dashboard" in current_url:
    # print("User is logged in and redirected to the dashboard page")
    driver.find_element(By.CLASS_NAME, 'css-1ljyfa8' .click())
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, 'Security Setting').click()
    current_url_security_setting = driver.current_url
    if 'security-setting' in current_url_security_setting:
        time.sleep(2)
        current_password_element = driver.find_element(By.NAME, 'currentPassword')
        new_password_element = driver.find_element(By.NAME, 'newPassword')
        confirm_password_element = driver.find_element(By.NAME, 'confirmPassword')

        current_password = "Sadiqkhang@123"
        new_password = "Sadiqkhang@1234"
        confirm_password = "Sadiqkhang@1234"

        # Check if any of the password fields are empty
        if not current_password or not new_password or not confirm_password:
            print("Please enter all password fields")
            driver.quit()
        else:
            # send the password values to the fields
            current_password_element.send_keys(current_password)
            new_password_element.send_keys(new_password)
            confirm_password_element.send_keys(confirm_password)

            # check if new password and confirm password match
            if new_password != confirm_password:
                print("New password and confirm password fields didn't match")
                driver.quit()
            else:
                # check the password requirements using regex pattern
                pattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$"
                if not re.match(pattern, new_password):
                    print("New password does not meet the required criteria")
                    # New password must contain 8 characters, one uppercase letter, one lowercase letter, one number, and one special character
                    driver.quit()
                else:
                    # check if new password is the same as the current password
                    if current_password == new_password:
                        print("New password must not be current password")
                        driver.quit()
                    else:
                        btn_element1 = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')

                        btn_element1.click()
                        # Password updated successfully
                        wait = WebDriverWait(driver, 10)
                        notification = wait.until(
                            EC.visibility_of_element_located((By.CLASS_NAME, 'Toastify__toast-body')))
                        # get the notification text
                        notification_text = notification.text

                        if "Password updated successfully" in notification_text:
                            print("Password update test passed")
                        else:
                            print("Password update test failed")
    else:
        print('User does not redirected to the security-setting page')

    driver.quit()
else:
    print("User login failed or was not redirected to the dashboard page")
    driver.quit()
# close the web driver instance
driver.quit()
