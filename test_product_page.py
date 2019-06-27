from .pages.product_page import ProductPage
import time


def test_guest_can_add_product_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    #time.sleep(1)
    page.check_message_product_added_to_basket()
    page.compare_product_price_to_basket_total()
