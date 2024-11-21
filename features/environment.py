from allure_behave.utils import scenario_name
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
#from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.options import Options

# after browswer stack use pls remove scenario_name from browser init(context)
from app.application import Application


# command to run allure and behave
# behave -f allure_behave.formatter:AllureFormatter -o test_results/ features


def browser_init(context):
    """
    :param context: Behave context
    """
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)


# chrome headless
# options = webdriver.ChromeOptions()
# options.add_argument('headless')
# service = Service(ChromeDriverManager().install())
# context.driver = webdriver.Chrome(
#     options=options,
#     service=service
# )
# firefox

# driver_path = GeckoDriverManager().install()
# service = Service(driver_path)
# context.driver = webdriver.Firefox(service=service)allure
# browser stack
# bs_user = ''
# bs_key = ''
# url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
#
# options = Options()
# bstack_options = {
#     "os": "Windows",
#     "osVersion": "11",
#     'browserName': 'chrome',
#     'sessionName': scenario_name
# }
# options.set_capability('bstack:options', bstack_options)
# context.driver = webdriver.Remote(command_executor=url, options=options)


    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
