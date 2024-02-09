from selenium import webdriver
import requests
import datetime


driver = webdriver.ChromeOptions()
driver.add_argument("--headless=new")


def test_status_code_200():
    # Заменяем дату
    date = "2024-01-01"

    # Формируем URL с учетом даты и API ключа
    url = f"https://api.nasa.gov/planetary/apod?api_key=NCCujGE8EdQRKyU6GjSNw98nMbFh03vgRo5Msoxd&date={date}"

    # Отправляем GET-запрос к API
    response = requests.get(url)

    # Получаем статусный код из ответа
    result = response.status_code

    # Проверяем, что статусный код находится в пределах 200-399 (включительно)
    assert 200 <= result < 400, f"Expected status code 2xx, but got {result}"
    result_json = (requests.get(url).json())


def test_first_data_status_code_200():
    # Заменяем дату
    date = "1995-06-16"

    # Формируем URL с учетом даты и API ключа
    url = f"https://api.nasa.gov/planetary/apod?api_key=NCCujGE8EdQRKyU6GjSNw98nMbFh03vgRo5Msoxd&date={date}"

    # Отправляем GET-запрос к API
    response = requests.get(url)

    # Получаем статусный код из ответа
    result = response.status_code

    # Проверяем, что статусный код находится в пределах 200-399 (включительно)
    assert 200 <= result < 400, f"Expected status code 2xx, but got {result}"

def test_first_data_status_code_400():
    # Заменяем дату
    date = "1995-06-15"

    # Формируем URL с учетом даты и API ключа
    url = f"https://api.nasa.gov/planetary/apod?api_key=NCCujGE8EdQRKyU6GjSNw98nMbFh03vgRo5Msoxd&date={date}"

    # Отправляем GET-запрос к API
    response = requests.get(url)

    # Получаем статусный код из ответа
    result = response.status_code

    # Проверяем, что статусный код находится в пределах от 400 (включительно)
    assert result >= 400, f"Expected status code 4xx, but got {result}"

def test_now_data_status_code_200():
    # Тут подтянется текущая дата
    date = datetime.date.today()

    # Формируем URL с учетом даты и API ключа
    url = f"https://api.nasa.gov/planetary/apod?api_key=NCCujGE8EdQRKyU6GjSNw98nMbFh03vgRo5Msoxd&date={date}"

    # Отправляем GET-запрос к API
    response = requests.get(url)

    # Получаем статусный код из ответа
    result = response.status_code

    # Проверяем, что статусный код находится в пределах 200-399 (включительно)
    assert 200 <= result < 400, f"Expected status code 2xx, but got {result}"

def test_status_code_400():
    # Заменяем дату на несуществующую
    date = "2024-31-31"

    # Формируем URL с учетом даты и API ключа
    url = f"https://api.nasa.gov/planetary/apod?api_key=NCCujGE8EdQRKyU6GjSNw98nMbFh03vgRo5Msoxd&date={date}"

    # Отправляем GET-запрос к API
    response = requests.get(url)

    # Получаем статусный код из ответа
    result = response.status_code

    # Проверяем, что статусный код находится в пределах 200-399 (включительно)
    assert result >= 400, f"Expected status code 4xx, but got {result}"

def test_status_code_api_key_bad():
    # Заменяем дату
    date = "2023-01-29"

    # Осознано делаем токен неправильным
    url = f"https://api.nasa.gov/planetary/apod?api_key=GE8EdQRKyU6GjSNw98nMbFh03vgRo5Msoxd&date={date}"

    # Отправляем GET-запрос к API
    response = requests.get(url)

    # Получаем статусный код из ответа
    result = response.status_code

    # Проверяем, что статусный код 403
    assert result == 403, f"Expected status code 4xx, but got {result}"




