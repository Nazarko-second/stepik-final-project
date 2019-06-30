from .base_page import BasePage
from .locators import CartPageLocators


NO_PRODUCTS_MESSAGE = ['Your basket is empty', 'Ваш кошик пустий', 'Ваша корзина пуста', 'Tu carrito esta vacío', 
                        'Votre panier est vide', 'Il tuo carrello è vuoto', 'Twój koszyk jest pusty']

class CartPage(BasePage):

    def check_there_are_no_products_in_cart(self):
        assert self.is_not_element_present(*CartPageLocators.PRODUCTS_LIST)

    def check_there_are_some_products_in_cart(self):
        assert self.is_element_present(*CartPageLocators.PRODUCTS_LIST)

    def should_be_text_cart_is_empty(self):
        message_full = self.browser.find_element(*CartPageLocators.EMPTY_CART_MESSAGE).text
        breakpoint_position = message_full.find(".")
        message = message_full[:breakpoint_position]
        if message in NO_PRODUCTS_MESSAGE:
            assert True
        else:
            assert False