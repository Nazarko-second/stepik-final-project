from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get("http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear")
product_price = browser.find_element_by_css_selector("p.price_color").text[1:]
basket_total_raw = browser.find_element_by_css_selector("div.basket-mini").text
basket_total = ''.join(c for c in basket_total_raw if c.isnumeric() or c == ".")
# print("product price ", product_price)
# print("basket total ", basket_total)
ALLERT_IN_BASKET = (By.CSS_SELECTOR, "p.price_color")
print(ALLERT_IN_BASKET)
allert = browser.find_element_by_css_selector("p.price_color")
print(allert)
print(allert.text)
browser.quit()