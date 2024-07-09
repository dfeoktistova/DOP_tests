import pytest
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_sbs(app):

    tests_count = 3
    app.add_sbs(tests_count)


    #test_id_and_name_sbs_1
    id_sbs_1 = app.find_elements("//*[@class='MuiTableCell-root MuiTableCell-body MuiTableCell-alignCenter "
                                 "MuiTableCell-sizeSmall']", 0).text
    name_sbs_1 = app.find_elements("//*[@class='MuiTableCell-root MuiTableCell-body MuiTableCell-alignCenter "
                                 "MuiTableCell-sizeSmall']", 1).text
    print('\n', 'ID НБС 1 - ', id_sbs_1, '\n', 'Название НБС 1 - ', name_sbs_1)
    assert id_sbs_1 == "1", 'Ошибка: Некорректный ID!'
    assert name_sbs_1 == "НБС 1", 'Ошибка: Некорректное название!'

    # test_id_and_name_sbs_2
    id_sbs_2 = app.find_elements("//*[@class='MuiTableCell-root MuiTableCell-body MuiTableCell-alignCenter "
                                "MuiTableCell-sizeSmall']", 2).text
    name_sbs_2 = app.find_elements("//*[@class='MuiTableCell-root MuiTableCell-body MuiTableCell-alignCenter "
                                   "MuiTableCell-sizeSmall']", 3).text
    print('\n', 'ID НБС 2 - ', id_sbs_2, '\n', 'Название НБС 2 - ', name_sbs_2)
    assert id_sbs_2 == "2", 'Ошибка: Некорректный ID!'
    assert name_sbs_2 == "НБС 2", 'Ошибка: Некорректное название!'

    # test_id_and_name_sbs_3
    id_sbs_3 = app.find_elements("//*[@class='MuiTableCell-root MuiTableCell-body MuiTableCell-alignCenter "
                                 "MuiTableCell-sizeSmall']", 4).text
    name_sbs_3 = app.find_elements("//*[@class='MuiTableCell-root MuiTableCell-body MuiTableCell-alignCenter "
                                   "MuiTableCell-sizeSmall']", 5).text
    print('\n', 'ID НБС 3 - ', id_sbs_3, '\n', 'Название НБС 3 - ', name_sbs_3)
    assert id_sbs_3 == "3", 'Ошибка: Некорректный ID!'
    assert name_sbs_3 == "НБС 3", 'Ошибка: Некорректное название!'
