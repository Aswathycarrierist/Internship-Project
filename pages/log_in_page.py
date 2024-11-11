from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class LogInPage(Page):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    EMAIL = "gopi.aswathy3@gmail.com"
    PASSWORD = "Dream*123"
    EMAIL_FIELD = (By.CSS_SELECTOR, "[placeholder='Email']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "[placeholder='Password']")
    LOGIN_BTN = (By.CSS_SELECTOR, "[wized='loginButton']")

    def enter_email(self):
        self.find_element(*self.EMAIL_FIELD).send_keys(self.EMAIL)

    def enter_password(self):
        self.find_element(*self.PASSWORD_FIELD).send_keys(self.PASSWORD)

    def click_log_in_button(self):
        self.wait.until(EC.element_to_be_clickable((self.LOGIN_BTN))).click()
