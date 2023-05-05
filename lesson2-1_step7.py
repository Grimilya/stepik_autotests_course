from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #Заполняем поля:
    x_element = browser.find_element(By.ID, 'treasure') 
    x = x_element.get_attribute('valuex')	# Значение Х
    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, '#answer') 
    input1.send_keys(y)	# Ответ
    option2 = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox') 
    option2.click()	# Отметить checkbox "I'm the robot"
    option3 = browser.find_element(By.CSS_SELECTOR, '#robotsRule') 
    option3.click()	# Выбрать radiobutton "Robots rule!"

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-default')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()