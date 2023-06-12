from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    #     Открыть страницу http://suninjuly.github.io/redirect_accept.html
    browser.get(link)

    #     Нажать на кнопку
    # time.sleep(2)
    # browser.execute_script("document.getElementsByTagName('button')[0].classList.remove('trollface');")
    # time.sleep(2)
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

    #     Переключиться на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    #     Пройти капчу для робота и получить число-ответ
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()
