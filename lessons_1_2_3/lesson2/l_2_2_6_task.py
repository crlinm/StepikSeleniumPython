import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://SunInJuly.github.io/execute_script.html"


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()

    # js для теста
    # browser.execute_script('document.title="Script executing";')

    # Открыть страницу https://SunInJuly.github.io/execute_script.html
    browser.get(link)

    # Считать значение для переменной x.
    x = browser.find_element(By.ID, "input_value").text

    # Посчитать математическую функцию от x.
    y = calc(x)

    # Проскроллить страницу вниз.
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.execute_script("window.scrollBy(0, 100);")

    # Ввести ответ в текстовое поле.
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    # Выбрать checkbox "I'm the robot".
    checkbox = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    print(checkbox.text)
    checkbox.click()

    # Переключить radiobutton "Robots rule!".
    radiobutton = browser.find_element(By.ID, "robotsRule")
    print(radiobutton.text)
    radiobutton.click()

    # Нажать на кнопку "Submit".
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit'")
    print(button.text)
    button.click()

finally:
    time.sleep(10)
    browser.quit()
