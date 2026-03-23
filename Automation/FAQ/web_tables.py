# Web Table: Print all rows and columns from a dynamic web table

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demoqa.com/webtables")

rows = driver.find_elements(By.XPATH, "//table//tr")

for i, row in enumerate(rows, start=1):
    cells =  row.find_elements(By.XPATH, ".//th | .//td")

    row_data = []

    for cell in cells:
        row_data.append(cell.text)

    print(f"Row {i}: {row_data}")
driver.quit()


'''
How it works
	•	//table//tr → gets all table rows
	•	.//th | .//td → gets all header and data cells inside each row
	•	Loop row by row
	•	Print each row’s cell values
'''