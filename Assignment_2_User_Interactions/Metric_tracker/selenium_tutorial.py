from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# New way to specify the path to the ChromeDriver using the Service class
chrome_driver_path = '/Users/romaricallahramadji/Documents/Platform_Computing/Assignment_2_User_Interactions /Metric_tracker/chromedriver'
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("http://localhost:3000/")

title = driver.title

# Recommended to use time.sleep for explicit waits or WebDriverWait for better practice
driver.implicitly_wait(0.5)

text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

text_box.send_keys("Selenium")
submit_button.click()

message = driver.find_element(by=By.ID, value="message")
text = message.text

#driver.quit()
while True:
    print()
