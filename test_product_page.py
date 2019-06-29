from pages.product_page import ProductPage
from pages.cart_page import CartPage
import time
import pytest

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = ["{}/?promo=offer{}".format(product_base_link, no) for no in range(10)]

# @pytest.mark.parametrize('link', urls)
# def atest_guest_can_add_product_to_cart(browser, link):
#     link = link
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_to_basket()
#     page.solve_quiz_and_get_code()
#     page.check_message_product_added_to_basket()
#     page.compare_product_price_to_basket_total()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, product_base_link)
    page.open()
    page.should_not_be_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page (browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_cart()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.check_there_are_no_products_in_cart()
    cart_page.should_be_text_cart_is_empty()