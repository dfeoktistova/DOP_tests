import time

import pytest
from fixture.application import Application
from data.UI.IP_address import IP_address_negative_data, IP_address_positive_data


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_accordions(app):

    # test accordion 1
    CHAPTER_1 = app.find_element("//*[text() = 'Настройки подключения НПДУ']")
    CHAPTER_1.click()
    time.sleep(2)
    BUTTON_NPDU_ACCORDION_BEFORE = app.find_elements("//*[@class='MuiButtonBase-root MuiAccordionSummary-root jss49 Mui-expanded jss48']", 0)
    aria_expanded_1_before = app.get_attribute_value(BUTTON_NPDU_ACCORDION_BEFORE, 'aria-expanded')
    assert aria_expanded_1_before == 'true', "Ошибка: Аккордеон не открыт"
    BUTTON_NPDU_ACCORDION_BEFORE.click()
    time.sleep(2)
    BUTTON_NPDU_ACCORDION_AFTER = app.find_elements("//*[@class='MuiButtonBase-root MuiAccordionSummary-root jss49']", 0)
    aria_expanded_1_after = app.get_attribute_value(BUTTON_NPDU_ACCORDION_AFTER, 'aria-expanded')
    assert aria_expanded_1_after == 'false', "Ошибка: Аккордеон не закрыт"

    # test accordion 2
    BUTTON_SBS_LIST_ACCORDION_BEFORE = app.find_elements("//*[@class='MuiButtonBase-root MuiAccordionSummary-root jss49 Mui-expanded jss48']", 0)
    aria_expanded_2_before = app.get_attribute_value(BUTTON_SBS_LIST_ACCORDION_BEFORE, 'aria-expanded')
    assert aria_expanded_2_before == 'true', "Ошибка: Аккордеон не открыт"
    BUTTON_SBS_LIST_ACCORDION_BEFORE.click()
    time.sleep(2)
    BUTTON_SBS_LIST_ACCORDION_AFTER = app.find_elements("//*[@class='MuiButtonBase-root MuiAccordionSummary-root jss49']",0)
    aria_expanded_2_after = app.get_attribute_value(BUTTON_SBS_LIST_ACCORDION_AFTER, 'aria-expanded')
    assert aria_expanded_2_after == 'false', "Ошибка: Аккордеон не закрыт"

    # test accordion 3
    BUTTON_DOP_PARAMS_ACCORDION_BEFORE = app.find_elements("//*[@class='MuiButtonBase-root MuiAccordionSummary-root jss49 Mui-expanded jss48']", 0)
    aria_expanded_3_before = app.get_attribute_value(BUTTON_DOP_PARAMS_ACCORDION_BEFORE, 'aria-expanded')
    assert aria_expanded_3_before == 'true', "Ошибка: Аккордеон не открыт"
    BUTTON_DOP_PARAMS_ACCORDION_BEFORE.click()
    time.sleep(2)
    BUTTON_DOP_PARAMS_ACCORDION_AFTER = app.find_elements("//*[@class='MuiButtonBase-root MuiAccordionSummary-root jss49']",0)
    aria_expanded_3_after = app.get_attribute_value(BUTTON_DOP_PARAMS_ACCORDION_AFTER, 'aria-expanded')
    assert aria_expanded_3_after == 'false', "Ошибка: Аккордеон не закрыт"

    # test accordion 4
    BUTTON_CONTROL_MODULE_ACCORDION_BEFORE = app.find_elements("//*[@class='MuiButtonBase-root MuiAccordionSummary-root jss49 Mui-expanded jss48']", 0)
    aria_expanded_4_before = app.get_attribute_value(BUTTON_CONTROL_MODULE_ACCORDION_BEFORE, 'aria-expanded')
    assert aria_expanded_4_before == 'true', "Ошибка: Аккордеон не открыт"
    BUTTON_CONTROL_MODULE_ACCORDION_BEFORE.click()
    time.sleep(2)
    BUTTON_CONTROL_MODULE_ACCORDION_AFTER = app.find_elements("//*[@class='MuiButtonBase-root MuiAccordionSummary-root jss49']",0)
    aria_expanded_4_after = app.get_attribute_value(BUTTON_CONTROL_MODULE_ACCORDION_AFTER, 'aria-expanded')
    assert aria_expanded_4_after == 'false', "Ошибка: Аккордеон не закрыт"
















'''CHAPTER_2 = app.find_element("//*[text() = 'Получить список НБС']")
    CHAPTER_2.click()
    BUTTON_SBS_LIST_ACCORDION = app.find_elements("//*[@class='MuiButtonBase-root MuiAccordionSummary-root jss49 Mui-expanded jss48']", 1)
    # Получить начальное значение параметра
    aria_expanded_2_before = app.get_attribute_value(BUTTON_SBS_LIST_ACCORDION, 'aria-expanded')
    print(aria_expanded_2_before)
    time.sleep(3)
    if aria_expanded_2_before == 'true':
        BUTTON_SBS_LIST_ACCORDION.click()
        aria_expanded_2_false = app.get_attribute_value(BUTTON_SBS_LIST_ACCORDION, 'aria-expanded')
        assert aria_expanded_2_false == 'false', "Ошибка: Аккордеон не закрыт"
    else:
        BUTTON_NPDU_ACCORDION.click()
        time.sleep(3)
        aria_expanded_1_true = app.get_attribute_value(BUTTON_NPDU_ACCORDION, 'aria-expanded')
        assert aria_expanded_1_true == 'true', "Ошибка: Аккордеон не открыт"



    CHAPTER_3 = app.find_element("//*[text() = 'Параметры DOP']")
    CHAPTER_3.click()
    BUTTON_DOP_PARAMS_ACCORDION = app.find_elements("//*[@class='MuiButtonBase-root MuiAccordionSummary-root jss49 Mui-expanded jss48']", 2)
    # Получить начальное значение параметра
    aria_expanded_3_before = app.get_attribute_value(BUTTON_DOP_PARAMS_ACCORDION, 'aria-expanded')
    print(aria_expanded_3_before)
    time.sleep(3)
    if aria_expanded_3_before == 'true':
        BUTTON_DOP_PARAMS_ACCORDION.click()
        aria_expanded_3_false = app.get_attribute_value(BUTTON_DOP_PARAMS_ACCORDION, 'aria-expanded')
        assert aria_expanded_3_false == 'false', "Ошибка: Аккордеон не закрыт"
    else:
        BUTTON_DOP_PARAMS_ACCORDION.click()
        time.sleep(3)
        aria_expanded_3_true = app.get_attribute_value(BUTTON_DOP_PARAMS_ACCORDION, 'aria-expanded')
        assert aria_expanded_3_true == 'true', "Ошибка: Аккордеон не открыт"



    CHAPTER_4 = app.find_element("//*[text() = 'Управление станциями']")
    CHAPTER_4.click()
    BUTTON_CONTROL_MODULE_ACCORDION = app.find_elements("//*[@class='MuiButtonBase-root MuiAccordionSummary-root jss49 Mui-expanded jss48']", 3)
    # Получить начальное значение параметра
    aria_expanded_4_before = app.get_attribute_value(BUTTON_CONTROL_MODULE_ACCORDION, 'aria-expanded')
    print(aria_expanded_4_before)
    time.sleep(3)
    if aria_expanded_4_before == 'true':
        BUTTON_CONTROL_MODULE_ACCORDION.click()
        aria_expanded_4_false = app.get_attribute_value(BUTTON_CONTROL_MODULE_ACCORDION, 'aria-expanded')
        assert aria_expanded_4_false == 'false', "Ошибка: Аккордеон не закрыт"
    else:
        BUTTON_CONTROL_MODULE_ACCORDION.click()
        time.sleep(3)
        aria_expanded_4_true = app.get_attribute_value(BUTTON_CONTROL_MODULE_ACCORDION, 'aria-expanded')
        assert aria_expanded_4_true == 'true', "Ошибка: Аккордеон не открыт"'''
