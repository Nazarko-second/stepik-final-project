# For some reason relative import works different on my 2 PCs
# One requires dots in front of folder name ".pages" and other doesn't.
# So, if you have errors regarding imports, please try both methods.

from pages.main_page import MainPage
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.cart_page import CartPage

# from .pages.main_page import MainPage
# from .pages.base_page import BasePage
# from .pages.login_page import LoginPage
# from .pages.cart_page import CartPage

import pytest
import time

@pytest.mark.login_guest
class TestLoginFromMainPage(object):

    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

def test_guest_should_see_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()


def test_guest_cant_see_product_in_cart_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = BasePage(browser, link)
    page.open()
    page.go_to_cart()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.check_there_are_no_products_in_cart()
    cart_page.should_be_text_cart_is_empty()


#print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__,__name__,str(__package__)))