import time
from selenium import webdriver
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Initialize Firebase Admin
cred = credentials.Certificate("/Users/romaricallahramadji/Documents/Platform_Computing/Assignment_3_Database/metrictracker-3571c-ab0b99a4f098.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# Initialize browser
driver = webdriver.Chrome()

# Navigate to your website
driver.get("http://localhost:3000/")

metrics = []
start_time = time.time()

# Example of a simplified loop, adapt as necessary
while True:  # presence_time < 50: # seconds
    current_time = time.time()
    presence_time = current_time - start_time
    scroll_height = driver.execute_script("return document.body.scrollHeight")
    current_scroll = driver.execute_script("return window.pageYOffset")

    # Example of collecting and printing metrics
    print(f"Presence time: {presence_time} seconds")
    print(f"Scrolled {current_scroll}/{scroll_height} pixels")

    # Store or send the metrics to Firestore
    doc_ref = db.collection('user_metrics').document()  # Create a new document
    doc_ref.set({
        'presence_time': presence_time,
        'scroll_height': scroll_height,
        'current_scroll': current_scroll,
        'timestamp': firestore.SERVER_TIMESTAMP  # Automatically set server-side timestamp
    })

 # Assume db is your Firestore client.
    docs = db.collection('user_metrics').order_by('timestamp').get()

    for doc in docs:
      data = doc.to_dict()
      formatted_timestamp = data['timestamp'].strftime('%H:%M:%S')
      presence_time = data['presence_time']
      scrolling_pixels = data.get('current_scroll', 0)  # Default to 0 if not present
    
      print(f"TIMESTAMP: {formatted_timestamp}, PRESENCE_TIME: {presence_time:.2f}, SCROLLING: {scrolling_pixels}")


    time.sleep(10)  # Adjust as necessary
