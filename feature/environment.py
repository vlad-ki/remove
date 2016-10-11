from os import getcwd
from selenium.webdriver.chrome import webdriver


def before_all(context):
    path = ('{}/chromedriver'.format(getcwd()))
    context.driver = webdriver.WebDriver(executable_path=path)


def after_all(context):
    context.driver.quit()
