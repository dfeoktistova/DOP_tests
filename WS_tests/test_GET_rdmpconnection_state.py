import requests
from fixture import application as app


rdmpconnectionstate_url = requests.get('http://127.0.0.1:6776/lnsdop/rdmpconnection/state')


def test_getmodes():

    app.print_WS_response(rdmpconnectionstate_url)
    app.assert_response_code(rdmpconnectionstate_url)
