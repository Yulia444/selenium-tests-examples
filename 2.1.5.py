import math
from selenium import webdriver
from time import sleep

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.PhantomJS()
    link = "http://suninjuly.github.io/math.html"
    browser.get(link)
    x_element = browser.find_element_by_tag_name('span[id="input_value"]')
    x = int(x_element.text)
    y = calc(x)
    print(y)
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
        