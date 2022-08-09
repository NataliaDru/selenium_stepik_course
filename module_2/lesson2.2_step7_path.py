from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/execute_script.html"

#current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
#print("you are here - " + current_dir)

#print("you are here - " + os.path.abspath(os.path.dirname(__file__)))

current_dir = os.path.abspath(__file__)   # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 

print("abspath is " + file_path)  # выведется путь до файла ВМЕСТЕ с исполняемым файлом + новый файл

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 

print("dirname is " + file_path) # выведется путь до исполняемого файла + имя нового файла

