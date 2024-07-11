import pytest
from fixture.application import Application
import requests
from data.WS.getdop import getdop_data


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

    usepseudomode_list = [True, False]

    count = 0
    for usepseudomode_list_state in usepseudomode_list:
        getdop_data['usepseudomode'] = usepseudomode_list[count]
        print('\n', getdop_data)
        getdop_request = requests.post(getdop_url, json=getdop_data)
        app.assert_response_code(getdop_request)
        count += 1