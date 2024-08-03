import time

from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from .base_page import BasePage

class SbisPage(BasePage):
    CONTACTS = (By.LINK_TEXT, "Контакты")
    TENSOR_BANNER = (By.XPATH, "//img[@alt='Разработчик системы СБИС — компания «Тензор»']")

    REGION = (By.XPATH, "//span[contains(@class, 'sbis_ru-Region-Chooser__text sbis_ru-link')]")
    SELECTED_REGION = (By.XPATH, "//span[@title='Камчатский край' and contains(@class, 'sbis_ru-link')]")
    PARTNERS_LIST = (By.XPATH, "//div[contains(@class, 'sbisru-Contacts-List__city')]")

    FOOTER_DOWNLOAD = (By.LINK_TEXT, "Скачать локальные версии")

    def go_to_contacts(self):
        self.find_element(self.CONTACTS).click()
        time.sleep(2)

    def click_on_tensor_banner(self):
        self.find_element(self.TENSOR_BANNER).click()

    def get_current_region(self):
        # for attempt in range(3):  # Пытаемся несколько раз в случае возникновения StaleElementReferenceException
        #     try:
        #         return self.find_element(self.REGION).text
        #     except StaleElementReferenceException:
        #         if attempt == 2:
        #             raise
        time.sleep(3)
        return self.find_element(self.REGION).text

    def change_region(self):
        self.find_element(self.REGION).click()
        self.find_element(self.SELECTED_REGION).click()
        time.sleep(3)

    def get_partners_list(self):
        return self.find_element(self.PARTNERS_LIST).text

    def go_to_download_section(self):
        self.scroll_to_element(self.find_element(self.FOOTER_DOWNLOAD))
        self.find_element(self.FOOTER_DOWNLOAD).click()
