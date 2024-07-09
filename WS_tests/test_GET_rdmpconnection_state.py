import requests
import pytest
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_getmodes(app):
    rdmpconnectionstate_url = requests.get('http://127.0.0.1:6776/lnsdop/rdmpconnection/state')

    app.print_WS_response(rdmpconnectionstate_url)
    app.assert_response_code(rdmpconnectionstate_url)
