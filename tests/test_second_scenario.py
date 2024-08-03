from pages.sbis_page import SbisPage

def test_change_region(browser):
    sbis_page = SbisPage(browser)

    # 1. Переход на https://sbis.ru/ в раздел "Контакты"
    sbis_page.go_to_site()
    sbis_page.go_to_contacts()

    # 2. Проверка определения региона (Ярославская обл.)
    initial_region = sbis_page.get_current_region()
    assert initial_region == "Ярославская обл.", f"Должен быть регион 'Ярославская обл.', но получен '{initial_region}'"
    partners_list = sbis_page.get_partners_list()
    assert partners_list == "Ярославль", f"Список партнеров некорректно отображается"

    # 3. Изменение региона на Камчатский край
    sbis_page.change_region()

    # 4. Проверка подставки Камчатского региона, списка партнеров
    # Проверка url и title
    new_region = sbis_page.get_current_region()
    assert new_region == "Камчатский край", "Регион не изменился на Камчатский край"
    partners_list = sbis_page.get_partners_list()
    assert partners_list == "Петропавловск-Камчатский", f"Список партнеров некорректно отображается"
    assert "kamchatskij-kraj" in browser.current_url, "url обновлен некорректно"
    assert "Камчатский край" in browser.title, "Title обновлен некорректно"