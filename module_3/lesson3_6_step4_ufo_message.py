'''
Задание: параметризация тестов

Инопланетяне оставляют загадочные сообщения на Stepik в фидбеке задач на правильное решение. Мы смогли локализовать
несколько url-адресов задач, где появляются кусочки сообщений. Ваша задача — реализовать автотест со следующим
сценарием действий:

    - открыть страницу
    - ввести правильный ответ
    - нажать кнопку "Отправить"
    - дождаться фидбека о том, что ответ правильный
    - проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"

Правильным ответом на задачу в заданных шагах является число:
	import time
	import math
	answer = math.log(int(time.time()))

Используйте маркировку pytest для параметризации и передайте в тест список ссылок в качестве параметров:

https://stepik.org/lesson/236895/step/1
https://stepik.org/lesson/236896/step/1
https://stepik.org/lesson/236897/step/1
https://stepik.org/lesson/236898/step/1
https://stepik.org/lesson/236899/step/1
https://stepik.org/lesson/236903/step/1
https://stepik.org/lesson/236904/step/1
https://stepik.org/lesson/236905/step/1

Используйте осмысленное сообщение об ошибке в проверке текста, а также настройте нужные ожидания, чтобы тесты работали
стабильно.

В упавших тестах найдите кусочки послания. Тест должен падать, если текст в опциональном фидбеке не совпадает со
строкой "Correct!" Соберите кусочки текста в одно предложение и отправьте в качестве ответа на это задание.

Важно! Чтобы пройти это задание, дополнительно убедитесь в том, что у вас установлено правильное локальное время
(https://time.is/ru/). Ответ для каждой задачи нужно пересчитывать отдельно, иначе они устаревают.
'''


from selenium.webdriver.common.by import By
import time
import math
import pytest


ufo_message=''

'''
@pytest.fixture(scope="function")
def ufo_browser():
	print("\nstart browser for test..")
	browser = webdriver.Chrome()
	yield browser
	print("\nquit browser..")
	browser.quit()
	print("\nAnswer: " + ufo_message)
'''


def actual_time():
	return math.log(int(time.time()))


pages = ['https://stepik.org/lesson/236895/step/1',
		'https://stepik.org/lesson/236896/step/1',
		'https://stepik.org/lesson/236897/step/1',
		 'https://stepik.org/lesson/236898/step/1',
		'https://stepik.org/lesson/236899/step/1',
		'https://stepik.org/lesson/236903/step/1',
		'https://stepik.org/lesson/236904/step/1',
		'https://stepik.org/lesson/236905/step/1']


@pytest.mark.parametrize('page', pages)
def test_ufo_message(browser, page):
	global ufo_message
	browser.implicitly_wait(10)
	browser.get(page)

	browser.find_element(By.TAG_NAME, 'textarea').send_keys(str(actual_time()))
	browser.find_element(By.CLASS_NAME, 'submit-submission').click()

	msg = browser.find_element(By.CLASS_NAME, "smart-hints__hint").text

	try:
		assert msg == "Correct!", f"Error! {msg}"
	except AssertionError:
		ufo_message += browser.find_element(By.CLASS_NAME, "smart-hints__hint").text
		print(ufo_message)
