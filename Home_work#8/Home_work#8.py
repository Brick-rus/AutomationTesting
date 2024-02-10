import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

def test_Potter():
    driver.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer')
    driver.implicitly_wait(2)
    element = driver.find_element(By.XPATH, "//select[@name='userSelect']")

    element.click()
    user = Select(element.find_element(By.XPATH, "//select[@name='userSelect']"))
    user.select_by_visible_text("Harry Potter")
    user_customer = user.first_selected_option.text

    button = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/form/button")
    button.click()

    driver.implicitly_wait(3)
    user_log = driver.find_element(By.CSS_SELECTOR,
                                   "body > div > div > div.ng-scope > div > div:nth-child(1) > strong > span").text
    driver.save_screenshot('result-1.png')
    assert user_customer == user_log


def test_zero_user():
    driver.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer')
    driver.implicitly_wait(2)

    try:
        selected_customer = '---Your Name---'
        customer_dropdown = Select(driver.find_element(By.XPATH, '//*[@id="userSelect"]'))
        customer_dropdown.select_by_visible_text(selected_customer)
        button = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/form/button')
        button.click()
    except:
        button = False
    driver.save_screenshot('zero_user.png')
    assert button == False
