# Verify that the user is able to buy a packages
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

# check if the expected text is in the URL
if "dashboard" in driver.current_url:
    # print("User is logged in and redirected to the dashboard page")
    driver.find_element(By.CLASS_NAME, 'css-1ljyfa8').click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, 'Security Setting').click()
    current_url_security_setting = driver.current_url
    if 'security-setting' in current_url_security_setting:
        # print('User is redirected to the security-setting page')
        time.sleep(2)

        # Buy Packages
        btn_clk = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Buy Package')]")))
        btn_clk.click()
        time.sleep(3)

        if 'packages' in driver.current_url:
            # print("User is redirected to the packages page")
            wait = WebDriverWait(driver, 20)

            btn_element = driver.find_element(By.XPATH, '//button[text()="Activated Again"]')
            btn_element.click()

            add_files_input =driver.find_element(By.ID,'uploadImages')
            add_files_input.send_keys('C:/laptop.png')
            time.sleep(8)

            upload_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[2]/div/div[1]/div[3]/button')))
            upload_btn.click()
            time.sleep(4)

            user_pck = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'User Package')]")))
            user_pck.click()
            time.sleep(6)

            if 'ThankYou' in driver.current_url:
                print('User is redirected to the ThankYou page')
            else:
                print('User is not redirected to the ThankYou page')

        else:
            print("User is not redirected to the packages page")

    else:
        print('User is not redirected to the security-setting page')
else:
    print("User login failed or was not redirected to the dashboard page")

# close the web driver instance
driver.quit()
