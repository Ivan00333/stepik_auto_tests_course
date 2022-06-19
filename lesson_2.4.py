from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))

button_book = driver.find_element(By.ID, "book")
button_book.click()

x = driver.find_element(By.ID, "input_value").text
y = calc(x)

input = driver.find_element(By.ID, "answer")
input.send_keys(y)

button = driver.find_element(By.ID, "solve")
button.click()