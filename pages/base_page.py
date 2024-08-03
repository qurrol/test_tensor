import time

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.base_url = "https://sbis.ru/"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator),
                                                       message=f"Не найден элемент по локатору {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.presence_of_all_elements_located(locator),
                                                       message=f"Не найдены элементы по локатору {locator}")

    def go_to_site(self):
        return self.browser.get(self.base_url)

    def scroll_to_element(self, element):
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(2)