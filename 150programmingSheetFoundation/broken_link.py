from selenium import webdriver
import requests

# Launch browser
driver = webdriver.Chrome()
driver.get("https://google.com")   # change URL

# Find all anchor tags
links = driver.find_elements("tag name", "a")

broken_links = []

for link in links:
    url = link.get_attribute("href")

    # Skip empty or invalid links
    if url is None or url.startswith("javascript") or url.startswith("mailto"):
        continue

    try:
        response = requests.get(url, timeout=5)
        if response.status_code >= 400:
            broken_links.append((url, response.status_code))
    except requests.exceptions.RequestException:
        broken_links.append((url, "Request Failed"))

driver.quit()

# Print result
if broken_links:
    print("Broken links found:")
    for link in broken_links:
        print(link)
else:
    print("No broken links found")