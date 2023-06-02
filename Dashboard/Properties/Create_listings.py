from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import pyautogui
from selenium.webdriver.support import expected_conditions as EC


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
    # print("User is logged in and redirected to the dashboard page")
    driver.find_element(By.CLASS_NAME,'css-1ljyfa8').click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT,'Properties').click()
    current_url_listing = driver.current_url
    if 'listing' in current_url_listing:
        time.sleep(2)
        # print('User successfully redirected to the properties page')
        driver.find_element(By.CLASS_NAME,'MuiButton-label').click()
        time.sleep(3)

        current_url_add_property = driver.current_url

        if 'add-property' in current_url_add_property:
            # print("User successfully redirected to the add-property page")
            # Find the 'Choose file' input element
            file_input = driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div/div/input')

            # Send the file path to the input element
            file_input.send_keys('C:/laptop.png')
            time.sleep(3)

            # find the 'Add files' button element
            add_files_input = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/input')
            add_files_input.send_keys('C:/laptop.png')
            time.sleep(4)

            # find the 'Add files' button element
            add_files_input_2 = driver.find_element(By.XPATH,'/html/body/div/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/input')
            add_files_input_2.send_keys('C:/laptop.png')
            time.sleep(4)

            # find the 'Add files' button element
            add_files_input_3 = driver.find_element(By.XPATH,'/html/body/div/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/input')
            add_files_input_3.send_keys('C:/laptop.png')
            time.sleep(4)

            driver.find_element(By.CLASS_NAME,'form-control').send_keys('i-11')
            time.sleep(4)

            li_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//li[contains(text(), 'I-11, Islamabad, Islamabad Capital Territory, Pakistan')]")))
            # click on the element
            li_element.click()
            time.sleep(4)

            next_btn = wait.until(EC.visibility_of_element_located((By.XPATH,"//button[contains(text(),'Next')]")))
            next_btn.click()
            time.sleep(4)
            current_url = driver.current_url
            if 'add-property-features' in current_url:
                print("User successfully redirected to the add-property-features page")
                driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Property Title"]').send_keys('Testing Property')

                #Property Type
                btn_clk = wait.until(EC.visibility_of_element_located((By.XPATH, "//p[contains(text(),'Commercial')]")))
                btn_clk.click()

                clk_prop_type = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="root"]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div/div/div/div[1]/div/div[4]/div/div')))
                clk_prop_type.click()

                sel_prop_type = wait.until(EC.visibility_of_element_located((By.XPATH,"//li[contains(text(),'Shop')]")))
                sel_prop_type.click()


                # Property Details
                clk_prop_detail = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="root"]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div/div/div/div[1]/div/div[5]/div/div/div')))
                clk_prop_detail.click()

                sel_prop_detail = wait.until(EC.visibility_of_element_located((By.XPATH,"//li[contains(text(),'Square Meters')]")))
                sel_prop_detail.click()
                driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Property Size"]').send_keys('25')

                # Price
                driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Total Price"]').send_keys('500000')

                # General Information
                gen_info = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="root"]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div/div/div/div[2]/div/div[1]/div/div/div/div/div')))
                gen_info.click()
                sel_gen_info = wait.until(EC.visibility_of_element_located((By.XPATH,"//li[contains(text(),'2023')]")))
                sel_gen_info.click()

                # Badrooms
                bad_room = driver.find_elements(By.CSS_SELECTOR,'#rooms')
                bad_room[0].send_keys("5")

                # Bathrooms
                bath_room = driver.find_elements(By.CSS_SELECTOR,'#rooms')
                bath_room[1].send_keys("4")

                # Property Features
                # Find and click on the <p> tags with the specified text
                driver.find_element(By.XPATH,"//p[contains(text(),'Study Room')]").click()
                driver.find_element(By.XPATH,"//p[contains(text(),'Drawing Room')]").click()
                driver.find_element(By.XPATH,"//p[contains(text(),'Furnished')]").click()
                driver.find_element(By.XPATH,"//p[contains(text(),'Swimming Pool')]").click()
                driver.find_element(By.XPATH,"//p[contains(text(),'Dining Room')]").click()
                driver.find_element(By.XPATH,"//p[contains(text(),'Laundary Room')]").click()
                driver.find_element(By.XPATH,"//p[contains(text(),'Central Cooling')]").click()
                driver.find_element(By.XPATH,"//p[contains(text(),'Lawn')]").click()
                driver.find_element(By.XPATH,"//p[contains(text(),'TV Lounge')]").click()
                driver.find_element(By.XPATH,"//p[contains(text(),'Kitchen')]").click()
                driver.find_element(By.XPATH,"//p[contains(text(),'Corner House')]").click()
                driver.find_element(By.XPATH,"//p[contains(text(),'Balcony')]").click()
                driver.find_element(By.XPATH,"//p[contains(text(),'Servant Quarter')]").click()
                driver.find_element(By.XPATH,"//p[contains(text(),'Parking Space')]").click()
                driver.find_element(By.XPATH,"//p[contains(text(),'Home Theatre')]").click()
                driver.find_element(By.XPATH,"//p[contains(text(),'Wifi')]").click()
                driver.find_element(By.XPATH,"//p[contains(text(),'Central Heating')]").click()
                driver.find_element(By.XPATH,"//p[contains(text(),'Store Room')]").click()
                time.sleep(4)

                # For utility
                driver.find_element(By.XPATH,"//p[contains(text(),'Electricity')]").click()
                driver.find_element(By.XPATH,"//p[contains(text(),'Gas')]").click()

                time.sleep(4)
                # Facing
                element = wait.until(EC.element_to_be_clickable((By.XPATH, '//p[not(contains(.,"South East"))][contains(.,"East")]')))
                element.click()

                # Description
                driver.find_element(By.CSS_SELECTOR,'textarea[placeholder="Description"]').send_keys("Testing testing testing testing testing")

                # Contact Details
                driver.find_element(By.CSS_SELECTOR,'input[placeholder="Phone Number"]').send_keys("3358756376")
                driver.find_element(By.CSS_SELECTOR,'input[placeholder="1 (702) 123-4567"]').send_keys("3358756376")

                driver.find_element(By.XPATH,"//p[contains(text(),'Featured')]").click()
                driver.find_element(By.XPATH,"//button[contains(text(),'Publish')]").click()


                time.sleep(4)

            else:
                print("User does not redirected to the add-property-features page")
        else:
            print("User does not redirected to the add-property page")
    else:
        print('User does not redirected to the properties page')

else:
    print("User login failed or was not redirected to the dashboard page")

# close the web driver instance
driver.quit()
