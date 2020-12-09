import pytest

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage

products = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
            # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
            # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
            # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
            # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
            # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
            # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
            # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
            # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]


@pytest.mark.parametrize('product', products)
def test_guest_can_add_product_to_basket(browser, product):
    page = ProductPage(browser, product)
    page.open()
    page.click_add_to_basket_button()
    page.solve_quiz_and_get_code()
    page.should_be_success_add_message()
    page.should_be_success_basket_message()


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0")
    page.open()
    page.click_add_to_basket_button()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_add_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0")
    page.open()
    page.should_not_be_success_add_message()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0")
    page.open()
    page.click_add_to_basket_button()
    page.solve_quiz_and_get_code()
    page.should_be_disappeared_success_add_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, link)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.open_basket()
    basket_page = BasketPage(browser, link)
    basket_page.should_be_empty_basket_message()
