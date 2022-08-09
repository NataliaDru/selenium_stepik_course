from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"
current_dir = os.path.abspath(os.path.dirname(__file__))   # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')

try:
	browser = webdriver.Chrome()
	browser.get(link)

	browser.find_element(By.NAME, "firstname").send_keys("Natalia")
	browser.find_element(By.NAME, "lastname").send_keys("Dru")
	browser.find_element(By.NAME, "email").send_keys("test@test.com")

	browser.find_element(By.ID, "file").send_keys(file_path)

	browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

finally:
	time.sleep(3)
	browser.quit()

'''
current_dir = os.path.abspath(__file__)   # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 

print("abspath is " + file_path)  # выведется путь до файла ВМЕСТЕ с исполняемым файлом + новый файл

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 

print("dirname is " + file_path) # выведется путь до исполняемого файла + имя нового файла
'''
