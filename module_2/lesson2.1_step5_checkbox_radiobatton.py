from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/math.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)

	x = str(math.log(abs(12*math.sin(int(browser.find_element(By.ID, "input_value").text)))))
	input1 = browser.find_element(By.ID, "answer")
	input1.send_keys(x)

	check1 = browser.find_element(By.ID, "robotCheckbox")
	check1.click()

	radio1 = browser.find_element(By.ID, "robotsRule")
	radio1.click()

	btn1 = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
	btn1.click()

finally:
	time.sleep(5)
	browser.quit()