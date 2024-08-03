from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DownloadPage(BasePage):
    FIND_WINDOWS = (By.XPATH, "//span[contains(text(), 'Windows')]")
    FIND_SBIS_PLUGIN = (By.XPATH, "//div[@class='controls-TabButton__caption' and text()='СБИС Плагин']")
    SBIS_PLUGIN = (By.XPATH, "//a[@class='sbis_ru-DownloadNew-loadLink__link js-link' and text()='Скачать (Exe 11.05 МБ) ']")

    def download_sbis_plugin(self):
        self.find_element(self.FIND_WINDOWS).click()
        self.find_element(self.FIND_SBIS_PLUGIN).click()
        download_link = self.find_element(self.SBIS_PLUGIN).get_attribute('href')
        return download_link

    def get_plugin_size_from_site(self):
        file_size_text = self.find_element(self.SBIS_PLUGIN).text
        size_in_mb = float(file_size_text.split()[2].replace(',', '.'))
        return size_in_mb