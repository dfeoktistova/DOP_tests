import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import random
import time


class Application:

    def __init__(self):
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.implicitly_wait(3)
        self.driver.set_window_size(1920, 1080)
        self.driver.get('file:///C:/Program%20Files/Cell.Nets/LnsJsEdition/Packages/LnsDop/client/index.html')
        time.sleep(5)

    def find_elements(self, locator, number):
        element = self.driver.find_elements("xpath", locator)[number]
        return element

    def find_element(self, locator):
        element = self.driver.find_element("xpath", locator)
        return element

    def input_data(self, field, test_data):
        field.send_keys(Keys.CONTROL + 'a')
        field.send_keys(Keys.DELETE)
        field.send_keys(test_data)

    def read_test_data_from_file(self, path):
        file_path = os.path.abspath(path)
        with open(file_path, 'r', encoding="UTF-8") as file:
            #lines = file.readlines()
            lines = file.read().splitlines()
        return lines


    def get_attribute_value(self, field, attribute):
        result = field.get_attribute(attribute)
        # print('\n', result)
        return result

    def add_sbs(self, count):
        add_button = self.find_element("//*[@title='Добавить']")
        for i in range(count):
            add_button.click()
            time.sleep(0.5)

    def state_pseudo_mode(self):
        pseudo_mode = self.find_elements("//*[@type='checkbox']", 0)
        pseudo_mode_state = pseudo_mode.is_selected()
        print('\n', 'Статус - ', pseudo_mode_state)
        return pseudo_mode_state

    def switch_pseudo_mode(self):
        pseudo_mode = self.find_elements("//*[@type='checkbox']", 0)
        pseudo_mode.click()
        time.sleep(3)

    def print_WS_response(self, request):
        response_all = request.json()
        print('\nОбщий ответ: ', response_all)

        response_code = request.json()['code']
        print('\nКод ответа: ', response_code)

        response_error = request.json()['error']
        print('\nТекст ошибки: ', response_error)

        response_data = request.json()['data']
        print('\nТело ответа: ', response_data)

    def assert_response_code(self, request):
        response_code = request.json()['code']
        assert response_code == 0, 'Ошибка в коде ответа!'

        response_error = request.json()['error']
        if response_error != None:
            print('\nТекст ошибки:', response_error)

    def random_sbs_positions_count(self):
        sbs_count = random.randint(0, 20)
        #print(sbs_count)
        sbs_positions = []
        for sbs in range(sbs_count):
            latitude = {'latitude': random.randint(0, 100)}
            longitude = {'longitude': random.randint(0, 100)}
            altitude = {'altitude': random.randint(0, 100)}
            sbs_position = {**latitude, **longitude, **altitude}
            sbs_positions.append(sbs_position)
        #print(sbs_positions)
        return sbs_positions

    def destroy(self):
        self.driver.quit()
