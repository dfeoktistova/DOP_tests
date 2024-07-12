import random
from data.UI.IP_address import IP_address_positive_data, IP_address_negative_data
import pytest
from fixture.application import Application
import requests
import string


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


rdmpconnection_url = 'http://127.0.0.1:6776/lnsdop/rdmpconnection'


def test_rdmpconnection_1(app):
    rdmpconnection_data = {
        "address": app.IP_generator(),
        "port": random.randrange(1, 65535),
        "name": random.choice(string.ascii_lowercase)
    }

    '''print('request_address = ', rdmpconnection_data['address'])
    print('request_port = ', rdmpconnection_data['port'])
    print('request_name = ', rdmpconnection_data['name'])'''

    rdmpconnection_request = requests.post(rdmpconnection_url, json=rdmpconnection_data)
    response_address = rdmpconnection_request.json()['data']['address']
    response_port = rdmpconnection_request.json()['data']['port']
    response_name = rdmpconnection_request.json()['data']['name']
    app.assert_response_code(rdmpconnection_request)

    '''print('response_address = ', rdmpconnection_data['address'])
    print('response_port = ', rdmpconnection_data['port'])
    print('response_name = ', rdmpconnection_data['name'])'''

    assert response_address == rdmpconnection_data['address'], "Ошибка: В ответе получен некорректный IP-адрес"
    assert response_port == rdmpconnection_data['port'], "Ошибка: В ответе получен некорректный порт"
    assert response_name == rdmpconnection_data['name'], "Ошибка: В ответе получено некорректное имя"


def test_rdmpconnection_2(app):
    rdmpconnection_data = {
        "address": random.choice(IP_address_positive_data),
        "port": random.randrange(1, 65535),
        "name": random.choice(string.ascii_lowercase)
    }

    rdmpconnection_request = requests.post(rdmpconnection_url, json=rdmpconnection_data)
    response_address = rdmpconnection_request.json()['data']['address']
    response_port = rdmpconnection_request.json()['data']['port']
    response_name = rdmpconnection_request.json()['data']['name']
    app.assert_response_code(rdmpconnection_request)

    assert response_address == rdmpconnection_data['address'], "Ошибка: В ответе получен некорректный IP-адрес"
    assert response_port == rdmpconnection_data['port'], "Ошибка: В ответе получен некорректный порт"
    assert response_name == rdmpconnection_data['name'], "Ошибка: В ответе получено некорректное имя"


def test_rdmpconnection_3(app):
    rdmpconnection_data = {
        "address": random.choice(IP_address_negative_data),
        "port": random.randrange(1, 65535),
        "name": random.choice(string.ascii_lowercase)
    }

    rdmpconnection_request = requests.post(rdmpconnection_url, json=rdmpconnection_data)
    response_address = rdmpconnection_request.json()['data']['address']
    response_port = rdmpconnection_request.json()['data']['port']
    response_name = rdmpconnection_request.json()['data']['name']
    app.assert_response_code(rdmpconnection_request)

    assert response_address == rdmpconnection_data['address'], "Ошибка: В ответе получен некорректный IP-адрес"
    assert response_port == rdmpconnection_data['port'], "Ошибка: В ответе получен некорректный порт"
    assert response_name == rdmpconnection_data['name'], "Ошибка: В ответе получено некорректное имя"