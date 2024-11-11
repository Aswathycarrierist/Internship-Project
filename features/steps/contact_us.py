from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then

from time import sleep


@given('Open reely main page')
def open_reely(context):
    context.app.main_page.open_main()
    # context.driver.get('https://soft.reelly.io')
    sleep(5)


@when('Log in to the page')
def log_in(context):
    context.app.log_in_page.enter_email()
    sleep(2)
    context.app.log_in_page.enter_password()
    sleep(2)
    context.app.log_in_page.click_log_in_button()
    sleep(2)
    #  #context.driver.find_element(By.CSS_SELECTOR, "[placeholder='Email']").send_keys('gopi.aswathy3@gmail.com')
    #  sleep(2)
    # # context.driver.find_element(By.CSS_SELECTOR, "[placeholder='Password']").send_keys('Dream*123')
    #  sleep(2)
    # # context.driver.find_element(By.CSS_SELECTOR, "[wized='loginButton']").click()
    sleep(5)


@when('Click on settings option')
def click_settings(context):
    context.app.contact_us_page.click_settings_option()
    # context.driver.find_element(By.XPATH,"//a[contains(@class, 'menu-button-block') and @href='/settings']").click()
    sleep(5)


# "[href='/settings']")

@when('Click on Contact us option')
def click_contact_us(context):
    context.app.contact_us_page.click_contact_us_option()

    # context.driver.find_element(By.CSS_SELECTOR, ".page-setting-block.w-inline-block[href='/contact-us']").click()


@when('Verify contact us page opened')
def verify_contact_us_page(context):
    expected_text = 'Join us in social media'
    context.app.contact_us_page.verify_contact_us(expected_text)


# actual_text = context.driver.find_element(By.CSS_SELECTOR, "[class='name-chat-text']").text
# assert expected_text == actual_text, f'Expected {expected_text} did not match actual {actual_text}'


@then('Verify there are at least 4 social media icons')
def verify_social_media_icons(context):
    context.app.contact_us_page.verify_social_media_icons()
    #social_media_icons = context.driver.find_elements(By.CSS_SELECTOR, "[class='contact-button w-inline-block']")
   # assert len(social_media_icons) == 4, f'expected 4 but got {len(social_media_icons)}'


@then('Verify “Connect the company” button is available and clickable')
def verify_connect_the_company_button(context):
    context.app.contact_us_page.verify_connect_the_company_button()
    #context.driver.wait.until(
      #  EC.element_to_be_clickable((By.CSS_SELECTOR, "[href='/payment/personal']")))
