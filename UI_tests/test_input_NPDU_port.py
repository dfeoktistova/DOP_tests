import pytest
from fixture.application import Application


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


def test_input_NPDU_port_positive(app):
    file_path = "../data/port_positive.txt"
    test_data = app.read_test_data_from_file(file_path)

    BUTTON_NPDU_SETTINGS = app.find_element("//*[text() = 'Настройки подключения НПДУ']")
    BUTTON_NPDU_SETTINGS.click()

    # Находим поле ввода
    field_NPDU_port = app.find_elements("//*[@class='MuiInputBase-input MuiInput-input']", 1)

    test_number = 1

    for data in test_data:
        app.input_data(field_NPDU_port, data)
        get_aria_invalid = app.get_attribute_value(field_NPDU_port, 'aria-invalid')
        positive_test(get_aria_invalid, test_number)
        test_number += 1


def test_input_NPDU_port_negative(app):
    file_path = "../data/port_negative.txt"
    test_data = app.read_test_data_from_file(file_path)

    BUTTON_NPDU_SETTINGS = app.find_element("//*[text() = 'Настройки подключения НПДУ']")
    BUTTON_NPDU_SETTINGS.click()

    # Находим поле ввода
    field_NPDU_port = app.find_elements("//*[@class='MuiInputBase-input MuiInput-input']", 1)

    test_number = 1

    for data in test_data:
        app.input_data(field_NPDU_port, data)
        get_aria_invalid = app.get_attribute_value(field_NPDU_port, 'aria-invalid')
        negative_test(get_aria_invalid, test_number)
        test_number += 1
