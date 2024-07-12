import time
import pytest
from fixture.application import Application
import random


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_delete_one_sbs(app):

    # delete sbs 1
    count = 1
    app.add_sbs(count)
    sbs_checkbox = app.find_elements("//*[@type='checkbox']", 2 + count)
    sbs_checkbox.click()
    delete_button = app.find_elements("//*[@class='MuiButtonBase-root MuiButton-root MuiButton-text']", 1)
    delete_button.click()

    # delete sbs 2
    count = 2
    app.add_sbs(count)
    sbs_checkbox = app.find_elements("//*[@type='checkbox']", 2 + count)
    sbs_checkbox.click()
    delete_button = app.find_elements("//*[@class='MuiButtonBase-root MuiButton-root MuiButton-text']", 1)
    delete_button.click()


def test_delete_all_sbs(app):
    count = random.randrange(1, 30)
    app.add_sbs(count)
    sbs_checkbox = app.find_elements("//*[@type='checkbox']", 2)
    sbs_checkbox.click()
    time.sleep(0.5)
    delete_button = app.find_elements("//*[@class='MuiButtonBase-root MuiButton-root MuiButton-text']", 1)
    delete_button.click()
