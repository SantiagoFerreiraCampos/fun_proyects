from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path="selenium\chromedriver.exe")
driver = webdriver.Chrome(service=service)

try:
    # Navigate to YouTube
    driver.get("https://www.youtube.com")

    # Search for a video
    search_box = driver.find_element(By.NAME, "search_query")
    search_box.send_keys("lofi hip hop beats")
    search_box.send_keys(Keys.RETURN)

    # Wait for results and click the first video
    time.sleep(2)  # Give the page time to load (can use WebDriverWait for better reliability)
    video = driver.find_element(By.XPATH, "//a[@id='video-title']")
    video.click()

    # Wait for the video to play and monitor for ads
    while True:
        try:
            # Wait for the "Skip Ads" button to appear, timeout after 5 seconds
            skip_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'ytp-skip-ad-button')]"))
            )
            
            skip_button.click()  # Click the "Skip Ads" button
            print("Ad skipped!")
        except:
            # If the button doesn't appear within 5 seconds, check if video is playing normally
            print("No ad to skip at the moment.")

        
        # Sleep briefly to avoid excessive polling
        time.sleep(5)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Clean up by closing the browser
    driver.quit()