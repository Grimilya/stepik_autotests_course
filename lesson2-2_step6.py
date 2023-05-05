from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #Заполняем поля:
    x_element = browser.find_element(By.ID, 'input_value') 
    x = x_element.text	# Значение Х
    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, '#answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", input1) 
    input1.send_keys(y)	# Ответ
    option2 = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox') 
    option2.click()	# Отметить checkbox "I'm the robot"
    option3 = browser.find_element(By.CSS_SELECTOR, '#robotsRule') 
    option3.click()	# Выбрать radiobutton "Robots rule!"
    
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()