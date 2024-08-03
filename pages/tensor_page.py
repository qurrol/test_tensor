import time

from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from .base_page import BasePage

class TensorPage(BasePage):
    POWER_OF_PEOPLE = (By.XPATH, "//p[text()='Сила в людях']")
    LEARN_MORE = (By.XPATH,
                  "//div[contains(@class, 'tensor_ru-Index__block4-content tensor_ru-Index__card')]//p[contains(@class, 'tensor_ru-Index__card-text')]//a[contains(@class, 'tensor_ru-link tensor_ru-Index__link')]")
    WORK_SECTION = (By.XPATH,
                    "//div[contains(@class, 'tensor_ru-container') and contains(@class, 'tensor_ru-section') and contains(@class, 'tensor_ru-About__block3')]//img")

    def check_power_of_people_block(self):
        return self.find_element(self.POWER_OF_PEOPLE), f"Блок 'Сила в людях' не найден"

    def go_to_learn_more(self):
        time.sleep(4)
        learn_more_element = self.find_element(self.LEARN_MORE)
        self.scroll_to_element(learn_more_element)
        learn_more_element.click()

        time.sleep(1)

    def check_work_section_images(self):
        images = self.find_elements(self.WORK_SECTION)
        image_sizes = []
        for img in images:
            try:
                width = img.get_attribute("width")
                height = img.get_attribute("height")
            except StaleElementReferenceException:
                img = self.find_element((By.XPATH, img.get_attribute("xpath")))
                width = img.get_attribute("width")
                height = img.get_attribute("height")

            image_sizes.append((width, height))

        for i, (width, height) in enumerate(image_sizes, start=1):
            print(f"{i}-ое изображение: ширина - {width} и высота - {height}")

        return image_sizes

