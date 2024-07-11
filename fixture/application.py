from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
import os
import ctypes
import getpass
from selenium.webdriver.common.by import By


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        width, height = self.get_screeninfo()
        DOP_client = self.find_DOP_client()
        self.driver.set_window_size(width, height)
        self.driver.get(DOP_client)
        #wait = WebDriverWait(self.driver, 15, poll_frequency=1)

        new_content_locator = ("xpath", "//*[text()='Расчёт тепловой карты точностей']")
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(new_content_locator))
        time.sleep(1)


        #wait.until(EC.visibility_of_element_located(("xpath", "//*[text() = 'Расчёт тепловой карты точностей']")))
        #time.sleep(5)


    def get_screeninfo(self):
        user32 = ctypes.windll.user32
        user32.SetProcessDPIAware()
        width = user32.GetSystemMetrics(0)
        height = user32.GetSystemMetrics(1)
        return width, height

    def find_DOP_client(self):
        user = getpass.getuser()
        client_dir = f'C:/Users/{user}/AppData/Roaming'
        dop_list = []
        for root, dirs, files in os.walk(client_dir):
            for dir in dirs:
                if dir.endswith('DopClient'):
                    dop_dir = os.path.join(root, dir)
                    dop_list.append(dop_dir)
        print(dop_list)
        index_file = f'{dop_list[0]}\index.html'
        print(index_file)
        return index_file

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
            # lines = file.readlines()
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
        # print(sbs_count)
        sbs_positions = []
        for sbs in range(sbs_count):
            latitude = {'latitude': random.randint(0, 100)}
            longitude = {'longitude': random.randint(0, 100)}
            altitude = {'altitude': random.randint(0, 100)}
            sbs_position = {**latitude, **longitude, **altitude}
            sbs_positions.append(sbs_position)
        # print(sbs_positions)
        return sbs_positions

    def destroy(self):
        self.driver.quit()
