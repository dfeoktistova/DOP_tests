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


def test_input_points_vertical_positive(app):
    file_path = "../data/points_positive.txt"
    test_data = app.read_test_data_from_file(file_path)

    # Находим поле ввода
    field_horizontal_points = app.find_elements("//*[@class='MuiInputBase-input MuiInput-input']", 1)

    test_number = 1

    for data in test_data:
        app.input_data(field_horizontal_points, data)
        get_aria_invalid = app.get_attribute_value(field_horizontal_points, 'aria-invalid')
        positive_test(get_aria_invalid, test_number)
        test_number += 1


def test_input_points_vertical_negative(app):
    file_path = "../data/points_negative.txt"
    test_data = app.read_test_data_from_file(file_path)

    # Находим поле ввода
    field_horizontal_points = app.find_elements("//*[@class='MuiInputBase-input MuiInput-input']", 1)

    test_number = 1

    for data in test_data:
        app.input_data(field_horizontal_points, data)
        get_aria_invalid = app.get_attribute_value(field_horizontal_points, 'aria-invalid')
        negative_test(get_aria_invalid, test_number)
        test_number += 1

