# запуск: pytest -s -v test_items.py  --language=es

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_button_is_visible(browser):
    try:
        page = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(page)

        btn = WebDriverWait(browser, 3).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "btn-add-to-basket"))
        )
    except TimeoutException:
        btn = None
    assert btn, "The button is not visible on the page"
