import time

import pytest
from fixture.application import Application
from data.UI.IP_address import IP_address_negative_data, IP_address_positive_data


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_input_NPDU_port(app):
    BUTTON_NPDU_SETTINGS = app.find_element("//*[text() = 'Настройки подключения НПДУ']")
    BUTTON_NPDU_SETTINGS.click()

    field_NPDU_IP_address = app.find_elements("//*[@class='MuiInputBase-input MuiInput-input']", 0)

    test_number = 1

    for data in IP_address_positive_data:
        app.input_data(field_NPDU_IP_address, data)
        get_aria_invalid = app.get_attribute_value(field_NPDU_IP_address, 'aria-invalid')
        result = app.UI_test_field_positive(get_aria_invalid, test_number)
        print(get_aria_invalid)
        print(result)
        test_number += 1
        assert get_aria_invalid == "false", 'Ошибка: Некорректное значение параметра "get_aria_invalid"!'

    for data in IP_address_negative_data:
        app.input_data(field_NPDU_IP_address, data)
        get_aria_invalid = app.get_attribute_value(field_NPDU_IP_address, 'aria-invalid')
        result = app.UI_test_field_negative(get_aria_invalid, test_number)
        print(get_aria_invalid)
        print(result)
        test_number += 1
        assert get_aria_invalid == "true", 'Ошибка: Некорректное значение параметра "get_aria_invalid"!'
