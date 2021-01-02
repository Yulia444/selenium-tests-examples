from selenium import webdriver
from time import sleep
import math

def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/get_attribute.html"
    browser.get(link)
    image = browser.find_element_by_id('treasure')
    value = image.get_attribute('valuex')
    x = int(value)
    y = calc(x)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()
    radiobutton = browser.find_element_by_id('robotsRule')
    radiobutton.click()
    button = browser.find_element_by_tag_name('button')
    button.click()
finally:
    sleep(5)
    browser.quit()