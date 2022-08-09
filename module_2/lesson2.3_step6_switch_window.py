'''
Задание: переход на новую вкладку

В этом задании после нажатия кнопки страница откроется в новой вкладке, нужно 
переключить WebDriver на новую вкладку и решить в ней задачу.

Сценарий для реализации выглядит так:

1. Открыть страницу http://suninjuly.github.io/redirect_accept.html
2. Нажать на кнопку
3. Переключиться на новую вкладку
4. Пройти капчу для робота и получить число-ответ

Если все сделано правильно и достаточно быстро (в этой задаче тоже есть 
ограничение по времени), вы увидите окно с числом. Отправьте полученное число 
в качестве ответа на это задание.
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

def fu(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:
	browser = webdriver.Chrome()
	browser.get(link)
	browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

	second_window = browser.window_handles[1]
	browser.switch_to.window(second_window)
	var = browser.find_element(By.ID, "input_value").text
	browser.find_element(By.ID, "answer").send_keys(fu(var))

	browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

finally:
	time.sleep(3)
	browser.quit()
