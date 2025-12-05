from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.locator import MainPagesLocators

class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPagesLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_page(self):
        assert self.is_element_present(*MainPagesLocators.LOGIN_LINK), "login link was not found on this page"
