# Verify that the user is able to delete agency successfully
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

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
    del_agency = driver.find_element(By.XPATH, "//button[text()='Delete Agency']")
    del_agency.click()
    time.sleep(4)
    yes_btn = driver.find_element(By.XPATH, "//button[text()='Yes']")
    yes_btn.click()
    # time.sleep(5)
    # Verify the presence of the toast message
    toast_locator = (By.CLASS_NAME, 'Toastify__toast-body')
    try:
        wait.until(EC.visibility_of_element_located(toast_locator))
        toast_message = driver.find_element(*toast_locator).text
        if "Successfully Deleted" in toast_message:
            print("Found successfully!")
        else:
            print("Failed to found the toast message.")
    except NoSuchElementException:
        print("Toast message not found.")

else:
    print("User login failed or was not redirected to the dashboard page")

# close the web driver instance
driver.quit()


