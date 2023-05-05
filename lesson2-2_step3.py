from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try: 
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #Заполняем поля:
    x_element = browser.find_element(By.ID, 'num1') 
    x = x_element.text	# Значение Х
    y_element = browser.find_element(By.ID, 'num2')
    y = y_element.text	# Значение Y

    s = str(int(x) + int(y))
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(s) # ищем элемент с суммой
    
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-default')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()