import requests
from fixture import application as app


getmodes_url = requests.get('http://127.0.0.1:6776/lnsdop/getmodes')


def test_getmodes():
    getmodes_url = requests.get('http://127.0.0.1:6776/lnsdop/getmodes')

    app.print_WS_response(getmodes_url)
    app.assert_response_code(getmodes_url)
