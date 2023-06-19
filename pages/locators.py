from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button[type='submit']")
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.col-sm-6.product_main .price_color")
    ADD_TO_CART_MESSAGE_NAME = (By.CSS_SELECTOR, "#messages > div:nth-child(1) .alertinner strong")
    ADD_TO_CART_MESSAGE_PRICE = (By.CSS_SELECTOR, "#messages > div:nth-child(3) .alertinner strong")
