from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/execute_script.html"

def fu(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:
	browser = webdriver.Chrome()
	browser.get(link)

	x = browser.find_element(By.ID, "input_value").text
	time.sleep(2)
	browser.execute_script("window.scrollBy(0, 100);")

	browser.find_element(By.ID, "answer").send_keys(fu(x))
	browser.find_element(By.ID, "robotCheckbox").click()

	browser.find_element(By.ID, "robotsRule").click()

	browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

finally:
	time.sleep(3)
	browser.quit()
