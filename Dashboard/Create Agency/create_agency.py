# Verify that the user is able to create an agency
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
    try:
        create_agnecy_btn = driver.find_element(By.XPATH, "//button[text()='Create Agency']")
        create_agnecy_btn.click()

        if 'agency-profile-setting' in driver.current_url:
            time.sleep(5)
            # print("User is redirected to the create agency page")
            driver.find_element(By.NAME,'agencyName').send_keys('Test agency')
            driver.find_element(By.NAME,'agencyOwner').send_keys('Sadiq agency')
            driver.find_element(By.NAME,'agencyEmail').send_keys('sadiqagency@gmail.com')
            driver.find_element(By.NAME,'telephone').send_keys('0511231231')
            driver.find_element(By.NAME,'agencyPhone').send_keys('923334545456')
            # driver.find_element(By.NAME,'agencyName').send_keys('Test agency') date

            # Get the current date
            current_date = date.today().strftime("%m-%d-%Y")

            # Locate the text field and enter the date
            text_field = driver.find_element(By.NAME,"agencyEstablished")
            # time.sleep(6)
            # text_field.clear()
            text_field.send_keys(current_date)
            time.sleep(8)
            driver.find_element(By.NAME,'fax_code').send_keys('1234')
            driver.find_element(By.NAME,'fax').send_keys('0123456789')

            add_img_1 = driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/form/div[1]/div[9]/div/div/div[1]/div/div/input')
            add_img_1.send_keys('C:/laptop.png')
            time.sleep(4)

            add_img_2 = driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/form/div[1]/div[9]/div/div/div[2]/div/div/input')
            add_img_2.send_keys('C:/laptop.png')
            time.sleep(4)

            driver.find_element(By.NAME,'agencyAddress').send_keys('Hangu')
            driver.find_element(By.NAME,'country').send_keys('Pakistan')
            driver.find_element(By.NAME,'agencyNTN').send_keys('1233211233212')
            driver.find_element(By.NAME,'agencyZipcode').send_keys('12345')
            driver.find_element(By.NAME,'agencyCity').send_keys('Peshawar')

            driver.find_element(By.NAME,'aboutAgency').send_keys('This is test agency')

            # add_img_3 = driver.find_element(By.XPATH,'//*[@id="uploadImages"]')
            # add_img_3.send_keys('C:/laptop.png')
            # time.sleep(7)
            wait = WebDriverWait(driver, 10)

            save_btn = driver.find_element(By.XPATH,'//div[contains(@class, "trending-btn")]/button[contains(@class, "btn") and contains(@class, "btn-signup") and contains(@class, "text-white")]')

            time.sleep(5)
            save_btn.click()
            time.sleep(7)
        else:
            print("User is not redirected to the create agency page")

    except NoSuchElementException:
        print("Create Agency button not found")

else:
    print("User login failed or was not redirected to the dashboard page")

# close the web driver instance
driver.quit()

