from .base_page import BasePage
from selenium.webdriver.common.by import By
from pages.locator import MainPageLocators
from .login_page import LoginPage

class MainPage(BasePage):

    def go_to_login_page(self):
        login_page = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_page.click()

    def should_be_login_page(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "login link was not found on this page"
