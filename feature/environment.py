from selenium.webdriver.chrome import webdriver


def before_all(context):
    path =  '/home/vk/doc/Python3/virtualenvs/env3.5/lib/python3.5/site-packages/selenium/webdriver/chrome/chromedriver'
    context.driver = webdriver.WebDriver(executable_path=path)

def after_all(context):
    context.driver.quit()
    

