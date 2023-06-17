from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    # Открыть страницу http://suninjuly.github.io/explicit_wait2.html
    browser.get(link)

    # Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    price_check = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    # Нажать на кнопку "Book"
    button = browser.find_element(By.ID, "book")
    button.click()

    # Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()
