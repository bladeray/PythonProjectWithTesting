from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    languages = {
        "ar": "سلة التسوق فارغة",
        "ca": "La seva cistella està buida.",
        "cs": "Váš košík je prázdný.",
        "da": "Din indkøbskurv er tom.",
        "de": "Ihr Warenkorb ist leer.",
        "en": "Your basket is empty.",
        "el": "Το καλάθι σας είναι άδειο.",
        "es": "Tu carrito esta vacío.",
        "fi": "Korisi on tyhjä",
        "fr": "Votre panier est vide.",
        "it": "Il tuo carrello è vuoto.",
        "ko": "장바구니가 비었습니다.",
        "nl": "Je winkelmand is leeg",
        "pl": "Twój koszyk jest pusty.",
        "pt": "O carrinho está vazio.",
        "pt-br": "Sua cesta está vazia.",
        "ro": "Cosul tau este gol.",
        "ru": "Ваша корзина пуста",
        "sk": "Váš košík je prázdny",
        "uk": "Ваш кошик пустий.",
        "zh-cn": "Your basket is empty.",
    }

    def should_be_empty_basket_message(self):
        language = self.browser.execute_script(
            "return window.navigator.userLanguage || window.navigator.language")
        assert self.browser.find_element(*BasketPageLocators.BASKET_MESSAGE).text.find(
            BasketPage.languages.get(language)) != -1, "Empty basket message is not found or incorrect"

    def should_not_be_empty_basket_message(self):
        language = self.browser.execute_script(
            "return window.navigator.userLanguage || window.navigator.language")
        assert self.browser.find_element(*BasketPageLocators.BASKET_MESSAGE).text.find(
            BasketPage.languages.get(language)) == -1, "Empty basket message is found"
