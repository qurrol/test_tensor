import os
import requests
from pages.sbis_page import SbisPage
from pages.download_page import DownloadPage


def test_third_scenario(browser):
    sbis_page = SbisPage(browser)
    download_page = DownloadPage(browser)

    # 1. Переход на https://sbis.ru/
    sbis_page.go_to_site()

    # 2. Нахождение в footer'е "Скачать локальные версии" и переход по ссылке
    sbis_page.go_to_download_section()

    # 3. Скачивание СБИС Плагина для windows (в ту же папку, где сам тест)
    download_url = download_page.download_sbis_plugin()
    response = requests.get(download_url)
    file_path = 'sbisplugin-setup-web.exe'

    # 4. Убеждение в том, что плагин скачен
    with open(file_path, 'wb') as file:
        file.write(response.content)

    # 5. Сравнивание размера скаченного файла в МБ (=3.64 МБ)
    web_plugin_size = download_page.get_plugin_size_from_site()
    download_plugin_size = os.path.getsize(file_path) / (1024 * 1024)
    print(f"Размер файла с сайта: {web_plugin_size} МБ")
    print(f"Размер скачанного файла: {download_plugin_size} МБ")
    assert abs(
        download_plugin_size - web_plugin_size) < 0.1, \
        f"Размер файла {download_plugin_size} МБ не соответствует ожидаемому {web_plugin_size} МБ"

