
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common import NoSuchElementException


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.python.org/")

elem = driver.find_element(By.ID, "id-search-field")
print('Элемент нашелся')
elem.click()
elem.send_keys("python 3.12")
elem.send_keys(Keys.ENTER)
driver.save_screenshot("python3.12.png")
print("Поиск прошел успешно")
url = driver.current_url
print(url)
# следующая страница
elem = driver.find_element(By.ID, "id-search-field")
elem.clear()
elem.send_keys("python 3.13")
elem.send_keys(Keys.ENTER)
elem = driver.find_element(By.XPATH, "/html/body/div/header/div/nav/ul/li[2]/a")
elem.click()
driver.save_screenshot("python.png")
driver.back()
driver.close()
print("Тест пройден")

