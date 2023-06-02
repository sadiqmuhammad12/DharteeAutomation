# Verify that the user is redirects to the Featured, Publish, Unpublish and Draft link
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

# get the current URL of the page
current_url = driver.current_url

# check if the expected text is in the URL
if "dashboard" in current_url:
    time.sleep(2)
    # print("User is logged in and redirected to the dashboard page")
    driver.find_element(By.CLASS_NAME, 'css-1ljyfa8').click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, 'Properties').click()
    current_url_listing = driver.current_url
    if 'listing' in current_url_listing:
        time.sleep(2)
        # print('User successfully redirected to the properties page')

        # wait for the Featured link to be visible
        featured_link = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[contains(text(),"Featured")]'))
        )
        featured_link.click()
        time.sleep(2)
        # wait for the Publish link to be visible
        publish_link = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[contains(text(),"Publish")]'))
        )
        publish_link.click()
        time.sleep(2)

        # wait for the Unpublish link to be visible
        unpublish_link = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[contains(text(),"Unpublish")]'))
        )
        unpublish_link.click()
        time.sleep(2)

        # wait for the Draft link to be visible
        draft_link = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[contains(text(),"Draft")]'))
        )
        draft_link.click()
        time.sleep(2)

        print('User successfully clicked on all links')
    else:
        print('User does not redirected to the properties page')

else:
    print("User login failed or was not redirected to the dashboard page")

# close the web driver instance
driver.quit()
