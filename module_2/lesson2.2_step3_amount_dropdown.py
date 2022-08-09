from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/selects1.html"

browser = webdriver.Chrome()
browser.get(link)

select = browser.find_element(By.TAG_NAME, "select")
select.click()
options = len(browser.find_elements(By.TAG_NAME, "option"))
print(options)
x = 1
amount = 0

while x < options-1:
	print(str(amount) + "    " + str(x))
	amount += int(browser.find_element(By.CSS_SELECTOR, f"[value='{x}']").text)
	x += 1

print(amount)
time.sleep(5)
browser.quit()




	#treasure = browser.find_element(By.CSS_SELECTOR, "img#treasure")
	#treasure_attribute = treasure.get_attribute("valuex")
	#print("value of people radio: ", people_checked)
	#assert people_checked is not None, "People radio is not selected by default"
	# assert people_checked == "true", "People radio is not selected by default"

	#asw = calc(treasure_attribute)

	#input1 = browser.find_element(By.ID, "answer")
	#input1.send_keys(asw)

	#check1 = browser.find_element(By.ID, "robotCheckbox")
	#check1.click()

	#radio1 = browser.find_element(By.ID, "robotsRule")
	#radio1.click()

	#btn1 = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
	#btn1.click()