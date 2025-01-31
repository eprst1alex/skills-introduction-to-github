import unittest
from unittest.mock import DEFAULT

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from constant import DEFAULT_WAIT_TIMEOUT


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
        """Проверка неудачного входа в систему."""

        try:
            success = True
            # Ввод логина
            username_field = WebDriverWait(self.web, 10).until(
                EC.presence_of_element_located((By.ID, 'user-name'))
            )
            username_field.send_keys('standard_user')

            # Ввод пароля
            password_field = self.web.find_element(By.ID, 'password')
            password_field.send_keys('wrong_pass')
            # wrong_pass

            # Нажатие кнопки логина
            login_button = self.web.find_element(By.ID, 'login-button')
            login_button.click()

            WebDriverWait(self.web, DEFAULT_WAIT_TIMEOUT).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'error-button'))
            )

        except TimeoutException as e:
            success = False

        if not success:
            self.fail(f"Test test_login_failed Failed")

    def test_login_success(self):
        try:
            success = True
            # Ввод логина
            username_field = WebDriverWait(self.web, DEFAULT_WAIT_TIMEOUT).until(
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
        except:
            success = False

        if not success:
            self.fail("Test test_login_success Failed")
