from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")

class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    # LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    # LOGIN_PASS = (By.CSS_SELECTOR, "#id_login-password")
    # LOGIN_SUBMIT_BTN = (By.CSS_SELECTOR, "button[name='login_submit']")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    # REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    # REGISTER_PASS = (By.CSS_SELECTOR, "#id_registration-password1")
    # REGISTER_PASS_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    # REGISTER_SUBMIT_BTN = (By.CSS_SELECTOR, "button[name='registration_submit']")

class ProductPageLocators(object):
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ALLERT_IN_BASKET = (By.CSS_SELECTOR, "#messages .alertinner")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    BASKET_TOTAL = (By.CSS_SELECTOR, "div.basket-mini")
