from pages.base_page import Page
from selenium.webdriver.common.by import By


class MainPage(Page):
    MAIN_MENU = (By.XPATH, "//div[@class='circle-gradient']")

    def open_main(self):
        self.open('https://soft.reelly.io')

    def click_main_menu(self):
        self.find_element(*self.MAIN_MENU).click()
