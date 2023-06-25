# Verify that the user is redirected to the virtual tours page
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")

driver = webdriver.Chrome(service=serv_obj)

driver.get("https://dev.dhartee.pk/")
driver.maximize_window()
Packages_link = driver.find_element(By.XPATH, "//p[text()='Virtual Tours']")
Packages_link.click()

time.sleep(4)
if 'tours' in driver.current_url:
    card = driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div/div[2]/a')
    card.click()

    WebDriverWait(driver, 10).until(lambda driver: len(driver.window_handles) > 1)

    driver.switch_to.window(driver.window_handles[1])

    if 'GulbergMall' in driver.current_url:
        print('User is redirected to the GulbergMall page')
    else:
        print("User does not redirected to the GulbergMall page")

    driver.close()
    driver.switch_to.window(driver.window_handles[0])
else:
    print("User does not redirected to the tours page")

# Close the web driver instance
driver.quit()



