import random
from fixture import application as app
import requests


def test_post_getmodules():
    # Запрашиваем доступные конфигурации и получаем рандомный ID для
    getmodes_url = 'http://127.0.0.1:6776/lnsdop/getmodes'
    getmodes_request = requests.get(getmodes_url)
    app.assert_response_code(getmodes_request)
    response_getmodes = getmodes_request.json()
    modes = response_getmodes['data']['modes']
    modules_count = len(modes)
    randon_index = random.randrange(0, modules_count)
    random_index = modes[randon_index]['modeid']

    getmodules_data = {
        "modeid": random_index}

    # Отправляем запрос информации по выбранному ID
    getmodules_url = 'http://127.0.0.1:6776/lnsdop/getmodules'
    getmodules_request = requests.post(getmodules_url, json=getmodules_data)
    app.assert_response_code(getmodules_request)
    getmodules_modeid = getmodules_request.json()['data']['modeid']
    #print(getmodules_modeid)
    assert getmodules_modeid == random_index, 'Ошибка! Получена информация по другому модулю!'
