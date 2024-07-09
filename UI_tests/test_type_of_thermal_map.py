import time
import pytest
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_type_thermal_map(app):
    BUTTON_TYPE_OF_THERMAl_CARD = app.find_elements(
        "//*[@class='MuiSelect-root MuiSelect-select MuiSelect-selectMenu MuiInputBase-input MuiInput-input']", 1)

    BUTTON_TYPE_OF_THERMAl_CARD.click()
    time.sleep(1)
    OPTION_GRADIENT = app.find_element("//li[text() = 'Градиент']")
    OPTION_GRADIENT.click()
    result = BUTTON_TYPE_OF_THERMAl_CARD.text
    # print('\n', 'Выбрано -', result)
    assert result == 'Градиент', 'Ошибка: Выбрана некорректная опция'

    BUTTON_TYPE_OF_THERMAl_CARD.click()
    time.sleep(1)
    OPTION_STEPMAP = app.find_element("//li[text() = 'Ступеньки']")
    OPTION_STEPMAP.click()
    result = BUTTON_TYPE_OF_THERMAl_CARD.text
    # print('\n', 'Выбрано -', result)
    assert result == 'Ступеньки', 'Ошибка: Выбрана некорректная опция'

    BUTTON_TYPE_OF_THERMAl_CARD.click()
    time.sleep(1)
    OPTION_CUTOFMAP = app.find_element("//li[text() = 'Отсечка']")
    OPTION_CUTOFMAP.click()
    result = BUTTON_TYPE_OF_THERMAl_CARD.text
    # print('\n', 'Выбрано -', result)
    assert result == 'Отсечка', 'Ошибка: Выбрана некорректная опция'
