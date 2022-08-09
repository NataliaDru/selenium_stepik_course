from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
	browser = webdriver.Chrome()
	browser.get(link)

	treasure = browser.find_element(By.CSS_SELECTOR, "img#treasure")
	treasure_attribute = treasure.get_attribute("valuex")
	#print("value of people radio: ", people_checked)
	#assert people_checked is not None, "People radio is not selected by default"
	# assert people_checked == "true", "People radio is not selected by default"

	asw = calc(treasure_attribute)

	input1 = browser.find_element(By.ID, "answer")
	input1.send_keys(asw)

	check1 = browser.find_element(By.ID, "robotCheckbox")
	check1.click()

	radio1 = browser.find_element(By.ID, "robotsRule")
	radio1.click()

	btn1 = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
	btn1.click()

finally:
	time.sleep(5)
	browser.quit()