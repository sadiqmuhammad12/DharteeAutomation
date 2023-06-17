# Verify that the user is able to update the profile setting
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
driver.find_element(By.CLASS_NAME, "form-control").send_keys("3333333333")

driver.find_element(By.ID, 'outlined-adornment-password').send_keys("Sadiq@123")
btn_element1 = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
btn_element1.click()

time.sleep(6)

# Check if the expected text is in the URL
if "dashboard" in driver.current_url:
    # print("User is logged in and redirected to the dashboard page")
    driver.find_element(By.CLASS_NAME, 'css-1ljyfa8').click()
    time.sleep(5)

    driver.find_element(By.LINK_TEXT, 'Profile Setting').click()
    time.sleep(5)
    if 'profile-setting' in driver.current_url:
        # print('User is redirected to the profile-setting page')
        # driver.find_element(By.CSS_SELECTOR, '.MuiSvgIcon-root.jss91').click()  # Click on the profile edit icon
        # driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div/div/div/button').click()
        # time.sleep(4)
        # add_image = driver.find_element(By.CLASS_NAME, 'MuiButton-contained')  # Click on the Add Image button
        # add_image.send_keys('C:/laptop.png')
        time.sleep(4)
        driver.find_element(By.NAME,'firstName').send_keys('sadiq')
        driver.find_element(By.NAME,'lastName').send_keys('khan')
        driver.find_element(By.NAME,'email').send_keys('sadiqmuhammad795@gmal.com')
        driver.find_element(By.NAME,'telephone').send_keys('0511234567')
        driver.find_element(By.NAME,'faxCode').send_keys('1234')
        driver.find_element(By.NAME,'faxNumber').send_keys('0123456789')

        time.sleep(6)
        # add_img = driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div/div/form/div[1]/div[8]/div/div/div[1]/div/div/p[1]')
        # add_img.send_keys('C:/laptop.png')

        # add_img = driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div/div/form/div[1]/div[8]/div/input')
        # add_img = driver.find_element(By.CLASS_NAME,'text-center.m-0')
        add_img_1 = driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div/div/form/div[1]/div[8]/div/div/div[1]/div/div/input')
        add_img_1.send_keys('C:/laptop.png')
        time.sleep(4)

        add_img_2 = driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div/div/form/div[1]/div[8]/div/div/div[2]/div/div/input')
        add_img_2.send_keys('C:/laptop.png')
        time.sleep(4)
        driver.find_element(By.NAME,'address').send_keys('Hangu')
        driver.find_element(By.NAME,'country').send_keys('Pakistan')
        driver.find_element(By.NAME,'ntn').send_keys('1233211233212')
        driver.find_element(By.NAME,'zipcode').send_keys('12345')
        driver.find_element(By.NAME,'city').send_keys('Hangu')
        driver.find_element(By.NAME,'bio').send_keys('This is testing description')
        driver.find_element(By.CLASS_NAME,'loadingButton ').click()
        time.sleep(5)
    else:
        print('User is not redirected to the profile-setting page')

else:
    print("User login failed or was not redirected to the dashboard page")

# Close the web driver instance
driver.quit()
