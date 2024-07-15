import requests
from fixture import application as app


def test_getmodes():
    getmodes_url = 'http://127.0.0.1:6776/lnsdop/getmodes'
    getmodes_request = requests.get(getmodes_url)

    app.print_WS_response(getmodes_request)
    app.assert_response_code(getmodes_request)
