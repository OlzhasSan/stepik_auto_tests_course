from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

service = Service("/Users/olzhas/Desktop/chromedriver")
browser = webdriver.Chrome(service=service)
browser.get("http://suninjuly.github.io/explicit_wait2.html")

buy = WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
submit = browser.find_element(By.ID, 'book')
submit.click()
browser.execute_script("window.scrollBy(0, 500);")
x = browser.find_element(By.ID, 'input_value').text
y = calc(x)
answer = browser.find_element(By.ID, 'answer')
answer.send_keys(y)
but = browser.find_element(By.ID, 'solve')
but.click()

time.sleep(5)
browser.quit()