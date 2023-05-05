from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # жмём кнопку
    button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
    button.click()

    # принимаем confirm
    confirm = browser.switch_to.alert
    confirm.accept()

    #Заполняем поля:
    x_element = browser.find_element(By.ID, 'input_value') 
    x = x_element.text	# Значение Х
    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, '#answer')
    input1.send_keys(y)	# Ответ
    
    # Отправляем
    button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()