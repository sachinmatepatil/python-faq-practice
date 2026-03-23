from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

driver = webdriver.Chrome() #starts chrome browser
driver.get("https://google.com") #loads the webpage

links = driver.find_elements(By.TAG_NAME,"a")

broken_links = []

for link in links:
    url = link.get_attribute("href")

    if url is None or url.startswith("javascript") or url.startswith("mailto"):
        continue

    try:
        response = requests.get(url, timeout=5)

        if response.status_code >= 400:
            broken_links.append((url, response.status_code))

    except requests.exceptions.RequestException:
        broken_links.append((url, "Request failed"))

driver.quit()

if broken_links:
    print("Broken links found:")
    for link in broken_links:
        print(link)
else:
    print("No broken links found")


"""
In interviews, they like when you use HEAD request instead of GET because it is faster.

Example improvement:
response = requests.head(url, timeout=5)
"""

'''
30-Second Interview Explanation

I collect all anchor tags using Selenium, extract the href attribute, skip JavaScript and mailto links, then send HTTP requests using the requests library and 
identify broken links based on status codes greater than or equal to 400.
'''

'''
WHAT
	•	webdriver → opens browser
	•	By → helps locate elements
	•	requests → sends HTTP requests

WHY
	•	Selenium → get UI elements (links)
	•	Requests → validate links via API call

👉 Selenium alone cannot tell if link is broken.
'''