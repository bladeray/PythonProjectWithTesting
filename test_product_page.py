import pytest

from pages.product_page import ProductPage

products = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]


@pytest.mark.parametrize('product', products)
def test_guest_can_add_product_to_basket(browser, product):
    page = ProductPage(browser, product)
    page.open()
    page.click_add_to_basket_button()
    page.solve_quiz_and_get_code()
    page.should_be_success_add_message()
    page.should_be_success_basket_message()
