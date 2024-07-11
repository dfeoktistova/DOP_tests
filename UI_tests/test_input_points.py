import pytest
from fixture.application import Application
from data.UI.points import points_negative_data, points_positive_data


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_input_points_horizontal(app):
    field_horizontal_points = app.find_elements("//*[@class='MuiInputBase-input MuiInput-input']", 0)

    test_number = 1

    for data in points_positive_data:
        app.input_data(field_horizontal_points, data)
        get_aria_invalid = app.get_attribute_value(field_horizontal_points, 'aria-invalid')
        result = app.UI_test_field_positive(get_aria_invalid, test_number)
        print(result)
        test_number += 1

    for data in points_negative_data:
        app.input_data(field_horizontal_points, data)
        get_aria_invalid = app.get_attribute_value(field_horizontal_points, 'aria-invalid')
        result = app.UI_test_field_negative(get_aria_invalid, test_number)
        print(result)
        test_number += 1


def test_input_points_vertical(app):
    field_horizontal_points = app.find_elements("//*[@class='MuiInputBase-input MuiInput-input']", 1)

    test_number = 1

    for data in points_positive_data:
        app.input_data(field_horizontal_points, data)
        get_aria_invalid = app.get_attribute_value(field_horizontal_points, 'aria-invalid')
        result = app.UI_test_field_positive(get_aria_invalid, test_number)
        print(result)
        test_number += 1

    for data in points_negative_data:
        app.input_data(field_horizontal_points, data)
        get_aria_invalid = app.get_attribute_value(field_horizontal_points, 'aria-invalid')
        result = app.UI_test_field_negative(get_aria_invalid, test_number)
        print(result)
        test_number += 1


