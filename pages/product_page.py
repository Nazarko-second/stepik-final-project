from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):

	def add_to_basket(self):
		add_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
		add_btn.click()

	def check_message_product_added_to_basket(self):
		assert "has been added to your basket" in self.browser.find_element(*ProductPageLocators.ALLERT_IN_BASKET).text, "Added to basket text is not presented"

	def compare_product_price_to_basket_total(self):
		basket_raw = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
		basket = ''.join(c for c in basket_raw if c.isnumeric())
		product = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text[1:].replace('.', '')
		assert basket == product