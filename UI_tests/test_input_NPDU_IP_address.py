import time

import pytest
from fixture.application import Application
from data.UI.IP_address import IP_address_negative_data, IP_address_positive_data


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def positive_test(attribute, test_number):
    if attribute == 'false':
        print('\nТест №', test_number, 'завершен успешно')
    else:
        print('\nТест №', test_number, 'завершен  с ошибкой')


def negative_test(attribute, test_number):
    if attribute == 'true':
        print('\nТест №', test_number, 'завершен успешно')
    else:
        print('\nТест №', test_number, 'завершен  с ошибкой')


def test_input_NPDU_port(app):
    BUTTON_NPDU_SETTINGS = app.find_element("//*[text() = 'Настройки подключения НПДУ']")
    BUTTON_NPDU_SETTINGS.click()

    field_NPDU_IP_address = app.find_elements("//*[@class='MuiInputBase-input MuiInput-input']", 0)

    test_number = 1

    for data in IP_address_positive_data:
        app.input_data(field_NPDU_IP_address, data)
        get_aria_invalid = app.get_attribute_value(field_NPDU_IP_address, 'aria-invalid')
        result = app.UI_test_field_positive(get_aria_invalid, test_number)
        print(result)
        test_number += 1

    for data in IP_address_negative_data:
        app.input_data(field_NPDU_IP_address, data)
        get_aria_invalid = app.get_attribute_value(field_NPDU_IP_address, 'aria-invalid')
        result = app.UI_test_field_negative(get_aria_invalid, test_number)
        print(result)
        test_number += 1
