from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep

LINK = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(LINK)
    num1 = int(browser.find_element_by_id('num1').text)
    num2 = int(browser.find_element_by_id('num2').text)
    sum_ = num1 + num2
    select = Select(browser.find_element_by_tag_name('select'))
    select.select_by_value(str(sum_))
    button = browser.find_element_by_tag_name('button')
    button.click()
finally:
    sleep(10)
    browser.quit()
