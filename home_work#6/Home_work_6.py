from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://calcus.ru/kalkulyator-ipoteki")

cost_estate = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/form/div[3]/div[2]/div/input")
cost_estate.send_keys("3250000")

initial_payment = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/form/div[4]/div[2]/div[1]/input")
initial_payment.send_keys("250000")

term_of_the_loan = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/form/div[7]/div[2]/div[1]/input")
term_of_the_loan.send_keys("30")

interest_rate = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/form/div[9]/div[2]/div[1]/input")
interest_rate.send_keys("5")

driver.execute_script("window.scrollTo(0, 100);")
time.sleep(2)
button = driver.find_element(By.XPATH, "//input[@value='Рассчитать']")
button.click()
time.sleep(2)
driver.execute_script("window.scrollTo(0, 600);")
driver.save_screenshot("calc_1.png")

driver.execute_script("window.scrollTo(0, 1200);")
time.sleep(3)
driver.save_screenshot("calc_2.png")

driver.close()
driver.quit()





# Код который был на занятиях тоже есть)

# import time
#
# from selenium import webdriver
# from selenium.common import NoSuchElementException
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# driver.get("https://calcus.ru/kalkulyator-ipoteki")
# driver.maximize_window()
#
# try:
#     driver.implicitly_wait(5)
#
#     property_values = driver.find_element(By.NAME, "cost")
#     initial_payment = driver.find_element(By.NAME, "start_sum")
#     loan_period = driver.find_element(By.NAME, "period")
#     interest_rate = driver.find_element(By.NAME, "percent")
#     submit_button = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/form/div[12]/div/input")
#
#     test_case = {"property_values": "2600000",
#                  "initial_payment": "1000000",
#                  "loan_period": "5",
#                  "interest_rate": "15"}
#
#     property_values.click()
#     property_values.send_keys(test_case['property_values'])
#     initial_payment.click()
#     initial_payment.send_keys(test_case['initial_payment'])
#     loan_period.click()
#     loan_period.send_keys(test_case['loan_period'])
#     interest_rate.click()
#     interest_rate.send_keys(test_case['interest_rate'])
#
#     driver.maximize_window()
#     driver.execute_script("window.scrollTo(0, 100)")
#     driver.execute_script("arguments[0].click();", submit_button)
#
#     wait = WebDriverWait(driver, timeout=10)
#     wait.until(EC.invisibility_of_element_located((By.XPATH, "//div[@class='loading-overlay']")))
#
#     driver.save_screenshot(f'HW_6_{test_case["property_values"]}_1.png')
#
#     driver.execute_script("window.scrollTo(0, 1200)")
#     wait = WebDriverWait(driver, timeout=10)
#     wait.until(EC.invisibility_of_element_located((By.XPATH, "//div[@class='loading-overlay']")))
#
#     # # Добавим небольшую задержку для уверенности, что все элементы прогрузились
#     # time.sleep(1)
#     driver.save_screenshot(f'HW_6_{test_case["property_values"]}_2.png')
#
#     print('Все элементы найдены!')
# except NoSuchElementException:
#     print("нет ни одного элемента")
# finally:
#     driver.quit()


