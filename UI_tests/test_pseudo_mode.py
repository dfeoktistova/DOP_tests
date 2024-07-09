import pytest
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_default_state_checkbox_pseudo_mode(app):
    # default state = -checked
    pseudo_mode_state = app.state_pseudo_mode()
    assert pseudo_mode_state == True, 'Ошибка: Некорректное дефолтное значение чек-бокса Псевдодальномерный режим'


def test_checkbox_pseudo_mode(app):

    pseudo_mode_state = app.state_pseudo_mode()

    # Если состояние не дефолтное => приводим к дефолтноему
    if pseudo_mode_state == False:
        app.switch_pseudo_mode()

    # switch off checkbox
    app.switch_pseudo_mode()
    pseudo_mode_state = app.state_pseudo_mode()
    assert pseudo_mode_state == False, 'Ошибка: Некорректное дефолтное значение чек-бокса Псевдодальномерный режим'

    # switch on checkbox
    app.switch_pseudo_mode()
    pseudo_mode_state = app.state_pseudo_mode()
    assert pseudo_mode_state == True, 'Ошибка: Некорректное дефолтное значение чек-бокса Псевдодальномерный режим'

