
from selenium import webdriver


def get_web_driver(url):

    # Initialize driver for Chrome Browser
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(url)
    driver.maximize_window()
    print(driver.current_url)
    return driver

