import requests
import pytest
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_getmodes(app):
    getmodes_url = requests.get('http://127.0.0.1:6776/lnsdop/getmodes')

    app.print_WS_response(getmodes_url)
    app.assert_response_code(getmodes_url)
