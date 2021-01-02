from selenium import webdriver
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from math import log, fabs, sin

LINK = "http://suninjuly.github.io/explicit_wait2.html"
try:
    browser = webdriver.Chrome()
    browser.get(LINK)
    button = browser.find_element_by_id('book')
    WebDriverWait(browser, 13).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    button.click()
    browser.execute_script("window.scrollBy(0, 300);")
    num = int(browser.find_element_by_id('input_value').text)
    result = str(log(fabs(12 * sin(num))))
    input_ = browser.find_element_by_tag_name('input')
    input_.send_keys(result)
    button = browser.find_element_by_id('solve')
    button.click()
except:
    sleep(10)
    browser.quit()
