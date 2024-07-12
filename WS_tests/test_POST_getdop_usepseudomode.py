from fixture import application as app
import requests
from data.WS.getdop import getdop_data

getdop_url = 'http://127.0.0.1:6776/lnsdop/getdop'


def test_post_usepseudomode_true():

    # Создаем рандомное количество НБС
    sbs_list = app.random_sbs_positions_count()
    getdop_data['topology'] = sbs_list

    usepseudomode_true = True
    getdop_data['usepseudomode'] = usepseudomode_true

    #print('\n', getdop_data)
    getdop_request = requests.post(getdop_url, json=getdop_data)
    app.assert_response_code(getdop_request)


def test_post_usepseudomode_false():
    # Создаем рандомное количество НБС
    sbs_list = app.random_sbs_positions_count()
    getdop_data['topology'] = sbs_list

    usepseudomode_true = False
    getdop_data['usepseudomode'] = usepseudomode_true

    # print('\n', getdop_data)
    getdop_request = requests.post(getdop_url, json=getdop_data)
    app.assert_response_code(getdop_request)
