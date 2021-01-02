from selenium import webdriver
import os
from time import sleep

LINK = "http://suninjuly.github.io/file_input.html"
DATA = ['Julia', 'Olkhovyk', 'olkhovyk_ak16@nuwm.edu.ua']

try:
    browser = webdriver.Chrome()
    browser.get(LINK)
    inputs = browser.find_elements_by_tag_name('input')
    for input_, value in zip(inputs, DATA):
        input_.send_keys(value)
    current_path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_path, 'bio.txt')
    choose_file = browser.find_element_by_id('file')
    choose_file.send_keys(file_path)
    button = browser.find_element_by_tag_name('button')
    button.click()
finally:
    sleep(10)
    browser.quit()
    