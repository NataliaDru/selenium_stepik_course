from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/math.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
	browser = webdriver.Chrome()
	browser.get(link)

	x = browser.find_element(By.ID, "input_value").text
	asw = calc(x)
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