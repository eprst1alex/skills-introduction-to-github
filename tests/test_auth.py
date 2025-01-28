import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options



class LoginTestCase(unittest.TestCase):

    def setUp(self):
        # Укажите путь к chromedriver.exe
        service = Service('chromedriver.exe')

        # Настройка опций Chrome
        options = Options()
        # options.add_argument('--headless')  # Раскомментируйте для фонового режима
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        # Инициализация драйвера
        self.web = webdriver.Chrome(options=options, service=service)

        # Открытие страницы
        self.web.get('https://www.saucedemo.com')


    def test_login_failed(self):
        # Ввод логина
        username_field = WebDriverWait(self.web, 10).until(
            EC.presence_of_element_located((By.ID, 'user-name'))
        )
        username_field.send_keys('standard_user')

        # Ввод пароля
        password_field = self.web.find_element(By.ID, 'password')
        password_field.send_keys('wrong_pass')

        # Нажатие кнопки логина
        login_button = self.web.find_element(By.ID, 'login-button')
        login_button.click()

        # Вывод ошибки
        error_box = self.web.find_element(By.CLASS_NAME, 'error-button')
        print(error_box.text)

    def test_login_success(self):
        # Ввод логина
        username_field = WebDriverWait(self.web, 10).until(
            EC.presence_of_element_located((By.ID, 'user-name'))
        )
        username_field.send_keys('standard_user')

        # Ввод пароля
        password_field = self.web.find_element(By.ID, 'password')
        password_field.send_keys('secret_sauce')

        # Нажатие кнопки логина
        login_button = self.web.find_element(By.ID, 'login-button')
        login_button.click()

        # Ожидание загрузки страницы с товарами
        inventory_items = WebDriverWait(self.web, 5).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'inventory_item'))
        )

        # Проверка, что количество товаров на странице больше нуля
        self.assertGreater(len(inventory_items), 0, "Товары не найдены на странице после входа")




