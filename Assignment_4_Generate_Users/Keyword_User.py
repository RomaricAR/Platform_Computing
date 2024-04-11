from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# The path to your ChromeDriver
webdriver_path = '/Users/romaricallahramadji/Documents/Platform_Computing/Assignment_2_User_Interactions/Metric_tracker/chromedriver'

# Create a Service object with the path to ChromeDriver
service = Service(webdriver_path)

# Initialize the WebDriver with the Service object
driver = webdriver.Chrome(service=service)

# The keyword you're looking for
keyword = 'student'

# The base time you spend on the website (in seconds)
base_presence_time = 10

# Navigate to the URL
driver.get("http://localhost:3000/")

# Time tracking for breaking the loop
start_time = time.time()
max_duration = 30  # Maximum duration to run the script in seconds

while True: 
    # Check if the keyword is in page source
    if keyword in driver.page_source:
        # If keyword is found, extend the presence time
        presence_time = base_presence_time + 10
        print(f"Keyword '{keyword}' found, extending presence time by {presence_time} seconds.")
    else:
        presence_time = base_presence_time
        print("No keyword found, no extension to presence time.")

    # Simulate presence time (wait)
    time.sleep(presence_time)

    # Check if the script has run for the maximum duration
    if time.time() - start_time > max_duration:
        print("Reached maximum script duration. Exiting.")
        break

# Close the browser
driver.quit()
