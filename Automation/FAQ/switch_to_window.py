#Window Handling: Write a program to switch to the third open window/tab.

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com")

driver.maximize_window()
driver.execute_script("window.open('https://www.google.com/');")
driver.execute_script("window.open('https://www.facebook.com/');")

windows = driver.window_handles
if len(windows) >= 3:
    driver.switch_to.window(windows[2])
    print("Current url", driver.current_url + driver.title)
else:
    print("Less than 3 windows are open")
time.sleep(2)
driver.quit()