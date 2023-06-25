# Verify that the user is redirected successfully with social media links
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")

driver = webdriver.Chrome(service=serv_obj)

driver.get("https://dev.dhartee.pk/")
driver.maximize_window()

# Find and click the "About" link
about_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='About']")))
about_link.click()

# Wait for the "About" page to load
WebDriverWait(driver, 10).until(EC.url_contains('about'))

# Define the social media links
links = [
    {"href": "https://www.facebook.com/dharteepk", "target": "_blank"},
    {"href": "https://www.instagram.com/dharteepk/", "target": "_blank"},
    {"href": "https://twitter.com/dharteepk", "target": "_blank"},
    {"href": "https://www.youtube.com/channel/UCVXsPliUOP6YmgDU3miaQ2g", "target": "_blank"},
    {"href": "https://play.google.com/store/apps/details?id=com.dhartee.codistan", "target": "_blank"},
    {"href": "https://apps.apple.com/us/app/dhartee/id1614198253", "target": "_blank"}
]

# Get the current window handle
main_window_handle = driver.current_window_handle

# Click on each link
for link in links:
    # Find the link element
    link_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, f'//a[@href="{link["href"]}"]'))
    )

    # Get the target attribute value
    target = link_element.get_attribute("target")

    # Open the link in a new tab if the target attribute is "_blank"
    if target == "_blank":
        # Execute JavaScript to click the link element
        driver.execute_script("arguments[0].click();", link_element)

        # Wait for the new tab to open
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

        # Switch WebDriver focus to the new tab
        for handle in driver.window_handles:
            if handle != main_window_handle:
                driver.switch_to.window(handle)
                break

        # Perform actions on the opened tab
        # For example, you can print the current URL
        print("Current URL:", driver.current_url)

        # Close the new tab
        driver.close()

        # Switch WebDriver focus back to the main window
        driver.switch_to.window(main_window_handle)

# Close the web driver instance
driver.quit()
