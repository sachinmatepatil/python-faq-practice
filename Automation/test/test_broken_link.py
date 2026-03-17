from selenium import webdriver
from Automation.pages.home_page import HomePage
from Automation.utils.broken_link import check_broken_links
from Automation.conftest import driver

def test_check_broken_links(driver):
    driver.get("https://google.com")

    home = HomePage(driver)
    links = home.get_links()

    broken_links = check_broken_links(links)

    assert len(broken_links) == 0, f"Broken link found: {broken_links}"

'''
🧠 Why This Is Strong (Interview Answer)
Separation of concerns:
Layer: Responsibility
Page :UI elements
Utils :Business logic
Test :Validation

🚀 Why This Is Industry Level
	•	Reusable components
	•	Clean separation
	•	Easy maintenance
	•	Scalable framework
	•	Matches real SDET work

⚡  Explanation

I structured the solution using Page Object Model where page classes handle UI elements, utilities handle link validation logic, and tests perform assertions. This ensures scalability, reusability, and clean separation of concerns.

'''