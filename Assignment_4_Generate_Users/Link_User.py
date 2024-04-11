from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, TimeoutException
import time

# Path to your ChromeDriver
webdriver_path = '/Users/romaricallahramadji/Documents/Platform_Computing/Assignment_2_User_Interactions/Metric_tracker/chromedriver'

# Initialize the WebDriver
service = Service(webdriver_path)
driver = webdriver.Chrome(service=service)

# Base presence time (in seconds)
base_presence_time = 10

def check_page(driver, depth=0, max_depth=2):
    if depth > max_depth:
        print("Reached maximum recursion depth.")
        return
    
    presence_time = base_presence_time

    # Check for images
    images = driver.find_elements(By.TAG_NAME, "img")
    if images:
        presence_time += 10 * len(images)
        print(f"Found {len(images)} images, extending presence time by {10 * len(images)} seconds.")
    
    # Check for the keyword 'student'
    if 'student' in driver.page_source:
        presence_time += 10
        print("Found keyword 'student', extending presence time by 10 seconds.")
    
    try:
        link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.TAG_NAME, "a")))
        driver.execute_script("arguments[0].scrollIntoView();", link)
        time.sleep(1)  # Wait for any overlays to adjust
        
        try:
            link.click()
        except ElementClickInterceptedException:
            driver.execute_script("arguments[0].click();", link)
        
        time.sleep(2)  # Wait for the page to load
        presence_time += 10
        print("Clicked a link, extending presence time by 10 seconds.")
        
        # Recursive call
        check_page(driver, depth + 1, max_depth)
    except (NoSuchElementException, TimeoutException) as e:
        print(f"No clickable link found")
    
    time.sleep(presence_time - base_presence_time)
    print(f"Total presence time: {presence_time} seconds at depth {depth}.")

# The URL to visit
url = "http://localhost:3000/"
print(f"Visiting: {url}")
driver.get(url)
check_page(driver)

# Close the browser
driver.quit()
