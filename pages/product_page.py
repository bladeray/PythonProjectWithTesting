from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_add_to_basket_button(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()

    def should_be_success_add_message(self):
        correct_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text + " has been added to your basket."
        assert self.browser.find_elements(*ProductPageLocators.SUCCESS_MESSAGES)[0].text.find(
            correct_message) != -1, "Success add message is not found or incorrect "

    def should_not_be_success_add_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGES), "Success message is presented, but should not be"

    def should_be_disappeared_success_add_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGES), "Success message is not disappeared, but should be"

    def should_be_success_basket_message(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert self.browser.find_element(*ProductPageLocators.INFO_MESSAGES).text.find(
            product_price) != -1, "Basket message is not found or incorrect"
