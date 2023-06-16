from selenium import webdriver
from selenium.webdriver.common.by import By

import os
import time

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()

    #   Открыть страницу http://suninjuly.github.io/file_input.html
    browser.get(link)

    #   Заполнить текстовые поля: имя, фамилия, email
    firstname = browser.find_element(By.NAME, "firstname")
    lastname = browser.find_element(By.NAME, "lastname")
    email = browser.find_element(By.NAME, "email")

    firstname.send_keys("name")
    lastname.send_keys("lastname")
    email.send_keys("email@mail.com")

    #   Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    input_file = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    print(input_file)

    current_dir = os.path.abspath(os.path.dirname(__file__))
    print(current_dir)
    file_path = os.path.join(current_dir, "file.txt")
    print(file_path)

    input_file.send_keys(file_path)

    #   Нажать кнопку "Submit"
    button = browser.find_element(By.TAG_NAME, "button")
    print(button)
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(10)
    browser.quit()
