from pages.sbis_page import SbisPage
from pages.tensor_page import TensorPage
import time

def test_first_scenario(browser):
    sbis_page = SbisPage(browser)
    tensor_page = TensorPage(browser)

    # 1. Переход на https://sbis.ru/ в раздел "Контакты"
    sbis_page.go_to_site()
    sbis_page.go_to_contacts()

    # 2. Поиск баннера Тензор и переход по нему
    sbis_page.click_on_tensor_banner()

    # 3. Явный переход на вкладку с url https://tensor.ru/
    browser.switch_to.window(browser.window_handles[-1])

    # 4. Проверка существования блока "Сила в людях"
    tensor_page.check_power_of_people_block()
    assert tensor_page, f"Блок 'Сила в людях' не найден"

    # 5. Переход в блок "Сила в людях" в "Подробнее" и где открывается https://tensor.ru/about
    tensor_page.go_to_learn_more()
    time.sleep(3)

    # 6. Проверка того, что у всех фотографий хронологии одинаковые height и width
    image_sizes = tensor_page.check_work_section_images()
    first_image_width, first_image_height = image_sizes[0]
    for i, (width, height) in enumerate(image_sizes):
        assert width == first_image_width, f"Ширина картинки {width} не равна ширине первой {first_image_width} для {i + 1}-ого изображения"
        assert height == first_image_height, f"Высота картинки {height} не равна высоте первой {first_image_height} для {i + 1}-ого изображения"
