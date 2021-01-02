from selenium import webdriver
from math import log, fabs, sin
from time import sleep

LINK = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(LINK)
    x = int(browser.find_element_by_id('input_value').text)
    result = log(fabs(12 * sin(x)))
    input_ = browser.find_element_by_tag_name('input')
    input_.send_keys(str(result))
    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()
    browser.execute_script("window.scrollBy(0, 200);")
    radiobutton = browser.find_element_by_id('robotsRule')
    radiobutton.click()
    button = browser.find_element_by_tag_name('button')
    button.click()
finally:
    sleep(10)
    browser.quit()