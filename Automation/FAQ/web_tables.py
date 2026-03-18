# Web Table: Print all rows and columns from a dynamic web table

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demoqa.com/webtables")

rows = driver.find_elements(By.XPATH, "//table //tr")

for i, row in enumerate(rows):
    cells =  row.find_elements(By.XPATH, ".//th | .//td")

    row_data = []

    for cell in cells:
        row_data.append(cell.text)

    print(f"Row {i}: {row_data}")
driver.quit()