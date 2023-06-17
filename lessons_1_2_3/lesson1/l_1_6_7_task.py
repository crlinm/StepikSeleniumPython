from selenium.webdriver.common.by import By
from selenium import webdriver
import time

URL = "http://suninjuly.github.io/huge_form.html"

try:
    browser = webdriver.Chrome()
    browser.get(URL)
    elements = browser.find_elements(By.CSS_SELECTOR, "input")
    for element in elements:
        element.send_keys("lala")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
