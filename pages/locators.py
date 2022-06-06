from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "#add_to_basket_form button[type='submit']")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main p.price_color")
    ALERT_PRODUCT_ADDED = (By.CSS_SELECTOR, "#messages div:nth-child(1)")
    ALERT_PRODUCT_ADDED_INNER_TXT = (By.CSS_SELECTOR, "#messages div:nth-child(1) .alertinner strong")
    ALERT_CART_PRICE = (By.CSS_SELECTOR, "#messages div:nth-child(3)")
    ALERT_CART_PRICE_TXT = (By.CSS_SELECTOR, "#messages div:nth-child(3) .alertinner strong")