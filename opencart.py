
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the webdriver
driver = webdriver.Firefox()
driver.maximize_window()
driver.get('https://demo-opencart.com')

# Find all elements with the class name 'product-thumb'
product_thumbs = driver.find_elements(By.CLASS_NAME, 'product-thumb')
print(f"Number of elements with class 'product-thumb': {len(product_thumbs)}")

# Find all menu items with the class name 'nav-item'
nav_items = driver.find_elements(By.CLASS_NAME, 'nav-item')
menu_names = [item.text for item in nav_items]
print("Menu items with class 'nav-item':")
for name in menu_names:
    print(name)

time.sleep(5)

# Close the WebDriver
driver.quit()

