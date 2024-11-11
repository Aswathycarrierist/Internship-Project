from pages.main_page import MainPage
from pages.base_page import Page
from pages.log_in_page import LogInPage
from pages.contact_us import ContactUsPage
class Application:
    def __init__(self,driver):
        self.page = Page(driver)
        self.main_page = MainPage(driver)
        self.log_in_page = LogInPage(driver)
        self.contact_us_page = ContactUsPage(driver)