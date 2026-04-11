#Basic Screenshot (Full Page Viewport)

from selenium import webdriver

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/")
driver.save_screenshot("screenshot.png")
driver.quit()

'''
🧠 What + Why
	•	save_screenshot() → captures current browser view
	•	Saves as .png file
	•	Useful for debugging failures / reports
'''

# Screenshot of Specific Element (Very Important
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://demoqa.com/')

element = driver.find_element(By.TAG_NAME, 'header')
element.screenshot('screenshot.png')
driver.quit()


# Screenshot on test failure
def screenshot_on_failure(driver):
    driver.get('https://demoqa.com/')
    try:
        assert "Wrongtile" in driver.title
    except:
        driver.save_screenshot('failure_screenshot.png')
        raise

#TimeStamp screenshot
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://demoqa.com/')
time_stamp = time.time()
driver.save_screenshot((f"screenshot_{time_stamp}.png"))
driver.quit()

'''
⏱ Complexity
	•	Time: O(1)
	•	Space: depends on image size
	
	I use driver.save_screenshot() to capture the browser state. For better debugging, I also capture element-level screenshots and attach them on test failure using pytest.
'''


'''
Say this in interview:
	•	“I integrate screenshots with Allure reports”
	•	“I capture screenshots on failure automatically”
	•	“I use element-level screenshots for better debugging”

'''