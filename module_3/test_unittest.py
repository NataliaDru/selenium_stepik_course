'''
Задание: оформляем тесты в стиле unittest 

Попробуйте оформить тесты из первого модуля в стиле unittest.

1. Возьмите тесты из шага — https://stepik.org/lesson/138920/step/11?unit=196194
2. Создайте новый файл
3. Создайте в нем класс с тестами, который должен наследоваться от unittest.TestCase по 
аналогии с предыдущим шагом
4. Перепишите в стиле unittest тест для страницы http://suninjuly.github.io/registration1.html
5. Перепишите в стиле unittest второй тест для страницы http://suninjuly.github.io/registration2.html
6. Оформите финальные проверки в тестах в стиле unittest, например, используя проверочный 
метод assertEqual
7. Запустите получившиеся тесты из файла 
8. Просмотрите отчёт о запуске и найдите последнюю строчку 
9. Отправьте эту строчку в качестве ответа на это задание 

Обратите внимание, что по задумке должно выбрасываться исключение NoSuchElementException 
во втором тесте. Если вы использовали конструкцию try/except, здесь нужно запустить тест 
без неё. Ловить исключения не надо (во всяком случае, здесь)!

Это всё для иллюстрации того, что unittest выполнит тесты и обобщит результаты даже при 
наличии неожиданного исключения. 
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestUnit(unittest.TestCase):
    def test_reg1(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")
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

        self.assertEqual("Congratulations! You have successfully registered!", text2, 
            "registration1 unsuccessfull")
        time.sleep(2)
        browser.quit()

    def test_reg2(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")
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

        self.assertEqual("Congratulations! You have successfully registered!", text2, 
            "registration2 unsuccessfull")
        time.sleep(2)
        browser.quit()
    
if __name__ == "__main__":
    unittest.main()
