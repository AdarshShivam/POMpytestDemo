from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.HomePage import HomePage

class LoginPage(BasePage):


    EMAIL = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "loginBtn")
    SIGNUP_LINK = (By.LINK_TEXT, "Sign up")

    def __init__(self, driver):
        # used to call parent class constructor
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """Page Actions"""
    def get_login_page_title(self, title):
        return  self.get_title(title)

    def is_signup_link_exist(self):
        return self.is_visible(self.SIGNUP_LINK)

    def do_login(self, username, password):
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BTN)
        return HomePage(self.driver)





