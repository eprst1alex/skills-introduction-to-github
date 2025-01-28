from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Укажите путь к chromedriver.exe
service = Service('chromedriver.exe')

# Настройка опций Chrome
options = Options()
# options.add_argument('--headless')  # Раскомментируйте для фонового режима
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# Инициализация драйвера
web = webdriver.Chrome(options=options, service=service)

# Открытие страницы
web.get('https://www.saucedemo.com')

try:
    # Ввод логина
    username_field = WebDriverWait(web, 10).until(
        EC.presence_of_element_located((By.ID, 'user-name'))
    )
    username_field.send_keys('standard_user')

    # Ввод пароля
    password_field = web.find_element(By.ID, 'password')
    password_field.send_keys('secret_sauce')

    # Нажатие кнопки логина
    login_button = web.find_element(By.ID, 'login-button')
    login_button.click()

    # Ожидание загрузки страницы с товарами
    WebDriverWait(web, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'inventory_item'))
    )

    # Поиск товара "Sauce Labs Backpack" и добавление его в корзину
    items = web.find_elements(By.CLASS_NAME, 'inventory_item')
    for item in items:
        item_name = item.find_element(By.CLASS_NAME, 'inventory_item_name').text
        if item_name == "Sauce Labs Backpack":
            add_to_cart_button = item.find_element(By.CLASS_NAME, 'btn_inventory')
            add_to_cart_button.click()
            print(f"Товар '{item_name}' добавлен в корзину.")
            break

    # Проверка, что товар добавлен в корзину
    cart_icon = web.find_element(By.CLASS_NAME, 'shopping_cart_link')
    cart_count = cart_icon.text

    if cart_count == "1":
        print("Товар успешно добавлен в корзину.")
    else:
        print("Ошибка: товар не добавлен в корзину.")


    # Оформление покупки
    web.get('https://www.saucedemo.com/cart.html')
    checkout_button = web.find_element(By.ID, 'checkout')
    checkout_button.click()
    # Ввод имени
    first_name_field = WebDriverWait(web, 10).until(
        EC.presence_of_element_located((By.ID, 'first-name'))
    )
    first_name_field.send_keys('Alex')

    # Ввод фамилии
    last_name_field = web.find_element(By.ID, 'last-name')
    last_name_field.send_keys('Grigorev')

    # Ввод индекса
    postal_field = web.find_element(By.ID, 'postal-code')
    postal_field.send_keys('1488')

    # Нажатие кнопки продолжить
    continue_button = web.find_element(By.ID, 'continue')
    continue_button.click()

    # Нажатие кнопки закончить
    finish_button = web.find_element(By.ID, 'finish')
    finish_button.click()


except Exception as e:
    print(f"Произошла ошибка: {e}")



finally:
    # Закрытие браузера
    web.quit()