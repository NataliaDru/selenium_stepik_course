# запуск теста для хрома - pytest -s -v --browser_name=chrome test_name.py
# запуск теста для файрфокса - pytest -s -v --browser_name=firefox test_name.py

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")
