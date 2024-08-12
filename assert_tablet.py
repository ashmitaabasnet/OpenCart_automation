from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the webdriver
driver = webdriver.Firefox()
driver.maximize_window()

# Open the demo OpenCart site
driver.get('https://demo-opencart.com')

# Find and click on the 'Tablets' link
tablets_link = driver.find_element(By.LINK_TEXT, 'Tablets')
tablets_link.click()

time.sleep(3)

# Assert that page loaded is tablets
assert 'path=57' in driver.current_url, "URL did not change to tablets page."

# Assert that the page title contains 'Tablets'
assert 'Tablets' in driver.title, "Page title does not contain 'Tablets'."

# Assert that the left navigation has a link or text related to tablets
left_nav = driver.find_element(By.ID, 'column-left')
assert 'Tablets' in left_nav.text, "Tablets not found in left navigation."

# Assert that the page heading is correct
page_heading = driver.find_element(By.XPATH, '//*[@id="content"]/h2')
assert 'Tablets' in page_heading.text, "Page heading does not contain 'Tablets'."

print("All assertions passed. The 'Tablets' page is loaded correctly.")

time.sleep(10)

# Close the WebDriver
driver.quit()


