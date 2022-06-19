from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

driver = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
driver.get(link)

try:
    button = driver.find_element(By.CLASS_NAME, "btn")
    button.click()

    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x = driver.find_element(By.ID, "input_value").text
    y = calc(x)
    input = driver.find_element(By.ID, "answer")
    input.send_keys(y)
    button = driver.find_element(By.CSS_SELECTOR, "[type = 'submit']")
    button.click()

finally:
    time.sleep(10)
    driver.quit()