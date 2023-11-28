import pytest
from Pages.LoginPage import LoginPage
from Config.config import TestData

@pytest.mark.usefixtures("init_driver")
class BaseTest:

    def test_home_page_title(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
