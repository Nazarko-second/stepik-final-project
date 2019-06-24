from .base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
	def go_to_login_page(self):
		login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
		login_link.click()

	def should_be_login_link(self):
		self.browser.find_element(By.CSS_SELECTOR, "#login_link"), "Login link is not presented"

#print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__,__name__,str(__package__)))