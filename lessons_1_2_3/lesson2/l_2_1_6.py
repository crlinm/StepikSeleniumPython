from selenium import webdriver
from selenium.webdriver.common.by import By

import math
import time

link = "http://suninjuly.github.io/math.html"


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()

    # Открыть страницу http://suninjuly.github.io/get_attribute.html.
    browser.get(link)

    people_radio = browser.find_element(By.ID, "peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print(type(people_checked), people_checked)
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"
    assert people_checked == "true", "People radio is not selected by default"

    robots_radio = browser.find_element(By.ID, "robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    print("robots_checked:", robots_checked)
    assert robots_checked is None

    # < button type = "submit" class ="btn btn-default" disabled > Submit < /button >
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    disabled = button.get_attribute("disabled")
    print("button disabled:", disabled)
    assert disabled is None

    # # Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
    # picture = browser.find_element(By.ID, "treasure")
    #
    # # Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
    # x = picture.get_attribute("valuex")
    #
    # # Посчитать математическую функцию от x (сама функция остаётся неизменной).
    # y = calc(x)
    #
    # # Ввести ответ в текстовое поле.
    # input_btn = browser.find_element(By.ID, "answer")
    # input_btn.send_keys(y)
    #
    # # Отметить checkbox "I'm the robot".
    # checkbox = browser.find_element(By.ID, "robotCheckbox")
    # checkbox.click()
    #
    # # Выбрать radiobutton "Robots rule!".
    # radiobutton = browser.find_element(By.ID, "robotsRule")
    # radiobutton.click()
    #
    # # Нажать на кнопку "Submit".
    # button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    # button.click()


finally:
    time.sleep(3)
    browser.quit()
