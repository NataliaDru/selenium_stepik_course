'''
Задание: принимаем alert

В этой задаче вам нужно написать программу, которая будет выполнять следующий 
сценарий:

1. Открыть страницу http://suninjuly.github.io/alert_accept.html
2. Нажать на кнопку
3. Принять confirm
4. На новой странице решить капчу для роботов, чтобы получить число с ответом

Если все сделано правильно и достаточно быстро (в этой задаче тоже есть 
ограничение по времени), вы увидите окно с числом. Отправьте полученное число 
в качестве ответа на это задание.
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"

def fu(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:
	browser = webdriver.Chrome()
	browser.get(link)

	browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
	browser.switch_to.alert.accept()

	var = browser.find_element(By.ID, "input_value").text
	browser.find_element(By.ID, "answer").send_keys(fu(var))
	browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

finally:
	time.sleep(3)
	browser.quit()
