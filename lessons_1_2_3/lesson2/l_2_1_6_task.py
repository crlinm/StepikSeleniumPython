from selenium import webdriver
from selenium.webdriver.common.by import By

import math
import time

link = "https://suninjuly.github.io/get_attribute.html"


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()

    # Открыть страницу http://suninjuly.github.io/get_attribute.html.
    browser.get(link)

    # Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
    picture = browser.find_element(By.ID, "treasure")

    # Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
    x = picture.get_attribute("valuex")
    print(x)
    print(type(x))

    # Посчитать математическую функцию от x (сама функция остаётся неизменной).
    y = calc(x)

    # Ввести ответ в текстовое поле.
    input_btn = browser.find_element(By.ID, "answer")
    input_btn.send_keys(y)

    # Отметить checkbox "I'm the robot".
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    # Выбрать radiobutton "Robots rule!".
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()

    # Нажать на кнопку "Submit".
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()


finally:
    time.sleep(10)
    browser.quit()
