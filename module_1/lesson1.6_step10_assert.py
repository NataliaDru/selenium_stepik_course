from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "http://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, ".first_block input.first")
    input1.send_keys("Kekich")
    input2 = browser.find_element(By.CSS_SELECTOR, ".first_block input.second")
    input2.send_keys("Lol")
    input3 = browser.find_element(By.CSS_SELECTOR, ".first_block input.third")
    input3.send_keys("Tbilisi")
    
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

    time.sleep(2)

    text1 = browser.find_element(By.TAG_NAME,"h1")
    text2 = text1.text

    assert "Congratulations! You have successfully registered!" == text2

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла