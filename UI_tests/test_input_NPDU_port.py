import pytest
from fixture.application import Application
from data.UI.port import port_negative_data, port_positive_data


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_input_NPDU_port(app):
    BUTTON_NPDU_SETTINGS = app.find_element("//*[text() = 'Настройки подключения НПДУ']")
    BUTTON_NPDU_SETTINGS.click()

    field_NPDU_port = app.find_elements("//*[@class='MuiInputBase-input MuiInput-input']", 1)

    test_number = 1

    for data in port_positive_data:
        app.input_data(field_NPDU_port, data)
        get_aria_invalid = app.get_attribute_value(field_NPDU_port, 'aria-invalid')
        result = app.UI_test_field_positive(get_aria_invalid, test_number)
        print(result)
        test_number += 1

    for data in port_negative_data:
        app.input_data(field_NPDU_port, data)
        get_aria_invalid = app.get_attribute_value(field_NPDU_port, 'aria-invalid')
        result = app.UI_test_field_negative(get_aria_invalid, test_number)
        print(result)
        test_number += 1
