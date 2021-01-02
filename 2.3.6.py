from selenium import webdriver
from time import sleep
from math import log, fabs, sin

LINK = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(LINK)
    button = browser.find_element_by_tag_name('button')
    button.click()
    next_window = browser.window_handles[1]
    browser.switch_to.window(next_window)
    num = int(browser.find_element_by_id('input_value').text)
    result = str(log(fabs(12 * sin(num))))
    input_ = browser.find_element_by_tag_name('input')
    input_.send_keys(result)
    button = browser.find_element_by_tag_name('button')
    button.click()
finally:
    sleep(10)
    browser.quit()