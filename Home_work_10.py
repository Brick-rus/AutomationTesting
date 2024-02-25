from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest


@pytest.fixture()
def driver():
    # -------------выполняется перед каждым тестом--------------#
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    yield driver


@pytest.mark.parametrize("login, password",
                         [("standard_user", "secret_sauce"),
                          ("problem_user", "secret_sauce"),
                          ("visual_user", "secret_sauce"), ]
                         )
def test_authorization_positiv(login, password, driver):
    user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
    user_name.send_keys(login)
    password_test = driver.find_element(By.XPATH, "//input[@id='password']")
    password_test.send_keys(password)
    button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
    button_login.click()
    result = driver.current_url
    assert result == "https://www.saucedemo.com/inventory.html"


@pytest.mark.parametrize("login, password",
                         [("standard_user", "secret"),
                          ("locked_out_user", "secret_sauce"),
                          ("", ""), ]
                         )
def test_authorization_negative(login, password, driver):
    user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
    user_name.send_keys(login)
    password_test = driver.find_element(By.XPATH, "//input[@id='password']")
    password_test.send_keys(password)
    button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
    button_login.click()
    result = driver.find_element(By.XPATH, "//div[@class='error-message-container error']")
    assert True == isinstance(result, object)


def test_business_process(driver):
    user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
    user_name.send_keys("standard_user")
    password_test = driver.find_element(By.XPATH, "//input[@id='password']")
    password_test.send_keys("secret_sauce")
    button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
    button_login.click()
    # Авторизация пройдена
    product = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
    value_product = product.text
    # Продукт найден
    product_purchase_button = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
    product_purchase_button.click()
    # Продукт в корзине
    basket = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
    basket.click()
    basket_product = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
    basket_product_result = basket_product.text
    # Проверка соответствия продукта в корзине и на публичной стороне
    assert value_product == basket_product_result
    checkout_button = driver.find_element(By.XPATH, "//button[@id='checkout']")
    checkout_button.click()
    # заполнение полей покупателя
    first_name = driver.find_element(By.XPATH, "//input[@id='first-name']")
    first_name.send_keys("Test")
    last_name = driver.find_element(By.XPATH, "//input[@id='last-name']")
    last_name.send_keys("Test")
    postal_code = driver.find_element(By.XPATH, "//input[@id='postal-code']")
    postal_code.send_keys("Test")
    continue_button = driver.find_element(By.XPATH, "//input[@id='continue']")
    continue_button.click()
    # Завершение покупки
    finish_button = driver.find_element(By.XPATH, "//button[@id='finish']")
    finish_button.click()
    order_creation = driver.find_element(By.XPATH, "//h2[@class='complete-header']")
    result = order_creation.text
    assert result == "Thank you for your order!"
    # Получение результата успешного окончания БП
