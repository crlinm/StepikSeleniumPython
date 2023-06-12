from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    # browser.get("http://suninjuly.github.io/registration2.html")
    browser.get("http://suninjuly.github.io/registration1.html")

    input1 = browser.find_element_by_css_selector("input[placeholder='Input your first name']")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector("input[placeholder='Input your last name']")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector("input[placeholder='Input your email']")
    input3.send_keys("test@test.com")

    # уникальные селекторы
    input4 = browser.find_element_by_xpath("//input[@id='country']")
    input4.send_keys("Russia")
    input5 = browser.find_element_by_css_selector("button.btn")
    input5.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)