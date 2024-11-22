from pages.base_page import Page
from pages.log_in_page import LogInPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class ContactUsPage(Page):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    PROFILE_ICON = (By.XPATH, "//a[@class='menu-photo_avatar w-inline-block' and @href='/settings']")
    CONTACT_US = (By.XPATH, "//div[@class='setting-text']")  # for mob  emulator

    SETTINGS = (By.XPATH, "//a[contains(@class, 'menu-button-block') and @href='/settings']")
    CONTACT_US = (By.CSS_SELECTOR, ".page-setting-block.w-inline-block[href='/contact-us']")#WEB
    #VERIFY_CONTACT = (By.CSS_SELECTOR, "[class='name-chat-text']")#WEB
    VERIFY_CONTACT = (By.XPATH, "//div[contains(@class, 'name-chat-text')]")

    # (By.XPATH, "//div[contains(@class, 'name-chat-text') and contains(text(), 'Join us in social media')]")

    SOCIAL_MEDIA_ICONS = (By.CSS_SELECTOR, "[class='contact-button w-inline-block']")
    CONNECT_COMPANY = (By.CSS_SELECTOR, "[href='/payment/personal']")

    def click_settings_option(self):
        self.wait.until(EC.element_to_be_clickable(self.SETTINGS)).click()

    def click_profile_icon(self):
        self.wait.until(EC.element_to_be_clickable(self.PROFILE_ICON)).click()

    def click_contact_us(self):
        self.wait.until(EC.element_to_be_clickable(self.CONTACT_US)).click()

    def verify_contact_us(self, expected_text):
        actual_text = self.driver.find_element(*self.VERIFY_CONTACT).text
        assert expected_text == actual_text, f'Expected {expected_text} did not match actual {actual_text}'

    def verify_social_media_icons(self):
        social_media_icons = self.driver.find_elements(*self.SOCIAL_MEDIA_ICONS)
        assert len(social_media_icons) == 4, f'expected 4 but got {len(social_media_icons)}'

    def verify_connect_the_company_button(self):
        connect_the_company_button = self.driver.find_element(*self.CONNECT_COMPANY)
        return
