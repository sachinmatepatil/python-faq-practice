# Dynamic Table Handling: Search for a specific value in a
# dynamic table
# and perform an action (edit/delete) on that row.
import time
from xxsubtype import bench

# simple script

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/webtables")

search_value = "Cierra"

rows = driver.find_elements((By.XPATH, "//table//th"))
for row in rows:
    if search_value in row.text:
        edit_button = row.find_element(By.XPATH, "//*[@id='edit-record-1']")
        edit_button.click()
        break
time.sleep(3)
driver.quit()
#time complexity - O(n) → scans rows once


#Reusable method
def perform_action(driver, search_value, action):
    rows = driver.find_elements(By.XPATH, "//table//th")
    for row in rows:
        if search_value in row.text:
            if action.lower() == "edit":
                row.find_element(By.XPATH, "//*[@id='edit-record-1']").click()
            elif action.lower() == "delete":
                row.find_element(By.XPATH, "//*[@id='delete-record-1']").click()
            return True
    return False
# Time Complexity - O(n) → scans rows once
# Space Complexity - O(1) - no extra space used