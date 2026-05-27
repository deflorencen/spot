from data.urls import Urls
from data.locators.auth_locator import AuthLocators
from pages.base_page import BasePage

class HomePage(BasePage):
    URL = Urls.HOME_PAGE

    def __init__(self, page):
        super().__init__(page)
        self.login_button = page.locator(AuthLocators.LOGIN_BUTTON)
        self.sign_up_button = page.locator(AuthLocators.SIGN_UP_BUTTON)