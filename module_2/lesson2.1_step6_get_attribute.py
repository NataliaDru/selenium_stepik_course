from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/math.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)

	people_radio = browser.find_element(By.ID, "peopleRule")
	people_checked = people_radio.get_attribute("checked")
	print("value of people radio: ", people_checked)
	assert people_checked is not None, "People radio is not selected by default"
	# assert people_checked == "true", "People radio is not selected by default"

	btn1 = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
	btn1.click()

finally:
	time.sleep(5)
	browser.quit()