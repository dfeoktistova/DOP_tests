from fixture import application as app
import requests
import random

def test_post_dopsettings_autosendrdmp_True():

    dopsettings_data_autosendrdmp_True = {
                            "autosendrdmp": True,
                            "visibleradiuskm": random.randint(0, 10000)
                        }

    autosendrdmp_request = dopsettings_data_autosendrdmp_True['autosendrdmp']
    visibleradiuskm_request = dopsettings_data_autosendrdmp_True['visibleradiuskm']

    dopsettings_url = 'http://127.0.0.1:6776/lnsdop/dopsettings'

    # Отправка запроса
    dopsettings_request_autosendrdmp_True = requests.post(dopsettings_url, json=dopsettings_data_autosendrdmp_True)

    app.assert_response_code(dopsettings_request_autosendrdmp_True)
    autosendrdmp_response = dopsettings_request_autosendrdmp_True.json()['data']['autosendrdmp']
    visibleradiuskm_response = dopsettings_request_autosendrdmp_True.json()['data']['visibleradiuskm']
    assert autosendrdmp_request == autosendrdmp_response, 'Ошибка: Некорректное значение параметра autosendrdmp в ответе'
    assert visibleradiuskm_request == visibleradiuskm_response, 'Ошибка: Некорректное значение параметра visibleradiuskm в ответе'


def test_post_dopsettings_autosendrdmp_False():

    dopsettings_data_autosendrdmp_True = {
                            "autosendrdmp": False,
                            "visibleradiuskm": random.randint(0, 10000)
                        }

    autosendrdmp_request = dopsettings_data_autosendrdmp_True['autosendrdmp']
    visibleradiuskm_request = dopsettings_data_autosendrdmp_True['visibleradiuskm']

    dopsettings_url = 'http://127.0.0.1:6776/lnsdop/dopsettings'

    # Отправка запроса
    dopsettings_request_autosendrdmp_True = requests.post(dopsettings_url, json=dopsettings_data_autosendrdmp_True)

    app.assert_response_code(dopsettings_request_autosendrdmp_True)
    autosendrdmp_response = dopsettings_request_autosendrdmp_True.json()['data']['autosendrdmp']
    visibleradiuskm_response = dopsettings_request_autosendrdmp_True.json()['data']['visibleradiuskm']
    assert autosendrdmp_request == autosendrdmp_response, 'Ошибка: Некорректное значение параметра autosendrdmp в ответе'
    assert visibleradiuskm_request == visibleradiuskm_response, 'Ошибка: Некорректное значение параметра visibleradiuskm в ответе'












