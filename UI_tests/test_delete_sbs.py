import time
import pytest
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_delete_sbs_1(app):
    count = 1
    app.add_sbs(count)
    sbs_checkbox = app.find_elements("//*[@type='checkbox']", 2 + count)
    sbs_checkbox.click()
    time.sleep(3)
    delete_button = app.find_elements("//*[@class='MuiButtonBase-root MuiButton-root MuiButton-text']", 1)
    delete_button.click()
    time.sleep(3)


def test_delete_sbs_2(app):
    count = 2
    app.add_sbs(count)
    sbs_checkbox = app.find_elements("//*[@type='checkbox']", 2 + count)
    sbs_checkbox.click()
    time.sleep(3)
    delete_button = app.find_elements("//*[@class='MuiButtonBase-root MuiButton-root MuiButton-text']", 1)
    delete_button.click()
    time.sleep(3)
