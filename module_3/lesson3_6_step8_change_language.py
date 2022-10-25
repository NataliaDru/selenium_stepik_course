# запуск -    pytest -s -v --browser_name=firefox/chrome test_name.py  --language=en/ru

import time
from selenium.webdriver.common.by import By


def test_lang(browser):
    page = "http://selenium1py.pythonanywhere.com/"
    browser.get(page)

    browser.find_element(By.CSS_SELECTOR, "#login_link")
    time.sleep(5)
