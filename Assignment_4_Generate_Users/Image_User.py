from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# Path to your ChromeDriver
webdriver_path = '/Users/romaricallahramadji/Documents/Platform_Computing/Assignment_2_User_Interactions/Metric_tracker/chromedriver'

# Create a Service object with the path to ChromeDriver
service = Service(webdriver_path)

# Initialize the WebDriver with the Service object
driver = webdriver.Chrome(service=service)

# URLs to test
urls = [
    "http://localhost:3000/",
    "https://rosswintle.uk/2016/11/websites-without-photos/"
]

# Base presence time (in seconds)
base_presence_time = 10

for url in urls:
    # Navigate to the URL
    driver.get(url)
    
    # Wait for the page to load
    time.sleep(2)  # Adjust as needed based on the website's load time
    
    # Find all <img> elements on the page
    images = driver.find_elements("tag name", "img")
    image_count = len(images)
    
    # Calculate the total presence time
    total_presence_time = base_presence_time + (10 * image_count)
    
    # Simulate presence time
    print(f"Visiting: {url}")
    print(f"Found {image_count} images, total presence time will be {total_presence_time} seconds.")
    time.sleep(total_presence_time)
    
    print("Moving to the next URL...\n")

# Close the browser
driver.quit()
