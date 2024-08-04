import os

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)
input1 = browser.find_element(By.NAME, "firstname")
input1.send_keys("Dasha")
input2 = browser.find_element(By.NAME, "lastname")
input2.send_keys("Bulycheva")
input3 = browser.find_element(By.NAME, "email")
input3.send_keys("DB")
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, "new.txt")
browser.find_element(By.CSS_SELECTOR, "#file").send_keys(file_path)

# Ваш код, который заполняет обязательные поля


# Отправляем заполненную форму
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()
