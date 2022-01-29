from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

# говорим Selenium ждать пока цена не упадёт до 100 баксов, это явный оператор ожидания
price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"),'$100'))

button1 = browser.find_element_by_id("book").click()

number = browser.find_element_by_id("input_value")
x = number.text
y = calc(x)

input1 = browser.find_element_by_id("answer").send_keys(y)
button2 = browser.find_element_by_id("solve").click()

time.sleep(15)
browser.quit()