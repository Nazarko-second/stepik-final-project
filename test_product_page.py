from pages.product_page import ProductPage
import time
import pytest

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = ["{}/?promo=offer{}".format(product_base_link, no) for no in range(6, 9)]

@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_cart(browser, link):
    link = link
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    #time.sleep(1)
    page.check_message_product_added_to_basket()
    page.compare_product_price_to_basket_total()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, product_base_link)
    page.open()
    page.should_not_be_success_message()

