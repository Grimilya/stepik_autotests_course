from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    #1
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/explicit_wait2.html')

    btn_book = browser.find_element(By.ID, 'book')

    #2 Чтобы определить момент, когда цена аренды уменьшится до $100, используйте метод text_to_be_present_in_element из библиотеки expected_conditions.
    moment = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    print('moment = ', moment)

    #3
    btn_book.click()

    # заполняем поля
    x_element = browser.find_element(By.ID, 'input_value') 
    x = x_element.text	# Значение Х
    y = calc(x)
    input1 = browser.find_element(By.ID, 'answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", input1) # проматываем вниз до элемента ввода
    input1.send_keys(y)	# Ответ
    
    # Отправляем
    button = browser.find_element(By.ID, 'solve')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()