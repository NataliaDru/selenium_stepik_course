# запускать командой pytest -s file_name.py
# -s отображает текст который выводится командой print()
'''
Рассмотрим два примера: создание экземпляра браузера и его закрытие только 
один раз для всех тестов первого тест-сьюта и создание браузера для каждого 
теста во втором тест-сьюте. Сохраните следующий код в файл test_fixture1.py  
и запустите его с помощью PyTest.

В первом тест-сьюте браузер запустился один раз, а во втором — два раза
Данные и кэш, оставшиеся от запуска предыдущего теста, могут влиять на 
результаты выполнения следующего теста, поэтому лучше всего запускать отдельный 
браузер для каждого теста, чтобы тесты были стабильнее. К тому же если вдруг 
браузер зависнет в одном тесте, то другие тесты не пострадают, если они 
запускаются каждый в собственном браузере.
'''

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

class TestMainPage1():

    @classmethod
    def setup_class(self):
        print("\nstart browser for test suite..")
        self.browser = webdriver.Chrome()

    @classmethod
    def teardown_class(self):
        print("quit browser for test suite..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")


class TestMainPage2():

    def setup_method(self):
        print("start browser for test..")
        self.browser = webdriver.Chrome()

    def teardown_method(self):
        print("quit browser for test..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")