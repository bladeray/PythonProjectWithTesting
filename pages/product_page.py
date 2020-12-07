from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_add_to_basket_button(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()

    def should_be_success_add_message(self):
        assert self.browser.find_elements(*ProductPageLocators.SUCCESS_MESSAGES)[0].text.find("has been added to your basket.") != -1, "Success message is not found"
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert self.browser.find_elements(*ProductPageLocators.SUCCESS_MESSAGES)[0].text.find(product_name) != -1, "Product name is not found in success message"

    def should_be_success_basket_message(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert self.browser.find_element(*ProductPageLocators.INFO_MESSAGES).text.find(product_price) != -1, "Basket message is not found or incorrect"