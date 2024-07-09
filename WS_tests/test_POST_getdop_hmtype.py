import pytest
from fixture.application import Application
import requests
from data.json_data.getdop import getdop_data


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_post_getdop(app):
    getdop_url = 'http://127.0.0.1:6776/lnsdop/getdop'

    # Создаем рандомное количество НБС
    sbs_list = app.random_sbs_positions_count()
    getdop_data['topology'] = sbs_list

    hmtype_list = ['gradient', 'stepmap', 'cutoffmap']

    count = 0
    for hmtype in hmtype_list:
        getdop_data['hmtype'] = hmtype_list[count]
        print('\n', getdop_data)
        getdop_request = requests.post(getdop_url, json=getdop_data)
        # app.print_WS_response(getdop_request)
        app.assert_response_code(getdop_request)
        count += 1