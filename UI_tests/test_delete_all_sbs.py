import time
import pytest
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_delete_all_sbs(app):
    count = 10
    app.add_sbs(count)
    sbs_checkbox = app.find_elements("//*[@type='checkbox']", 2)
    sbs_checkbox.click()
    time.sleep(1)
    delete_button = app.find_elements("//*[@class='MuiButtonBase-root MuiButton-root MuiButton-text']", 1)
    delete_button.click()
    time.sleep(1)
