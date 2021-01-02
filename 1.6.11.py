from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

WINDOW_SIZE = "1366,768"
CHROME_OPTIONS = Options()
#CHROME_OPTIONS.add_argument("--headless")
CHROME_OPTIONS.add_argument(f"--window-size={WINDOW_SIZE}")

DATA = ['Julia', 'Olkhovyk', 'julia@example.py']
LINKS = ["http://suninjuly.github.io/registration1.html",
        'http://suninjuly.github.io/registration2.html']

INPUTS = ["//div[@class='first_block']/div[@class='form-group first_class']/input",
          "//div[@class='first_block']/div[@class='form-group second_class']/input",
          "//div[@class='first_block']/div[@class='form-group third_class']/input"
]


def test1():
    # Test 1: Succesfull registration
    try:
        link = LINKS[0]
        browser = webdriver.Chrome(chrome_options=CHROME_OPTIONS)
        browser.get(link)
        inputs = []
        input1 = browser.find_element(By.XPATH, INPUTS[0])
        input2 = browser.find_element(By.XPATH, INPUTS[1])
        input3 = browser.find_element(By.XPATH, INPUTS[2])
        inputs.extend([input1, input2, input3])
        for input_, value in zip(inputs, DATA):
            input_.send_keys(value)
        button = browser.find_element_by_tag_name('button')
        button.click()
        response_text = browser.find_element_by_tag_name('h1')
        assert response_text.text == 'Congratulations! You have successfully registered!'
    finally:
        sleep(5)
        browser.quit()


def test2():
    # Test2: NoSuchElementException
    try:
        link = LINKS[1]
        browser = webdriver.Chrome(chrome_options=CHROME_OPTIONS)
        browser.get(link)
        inputs = []
        input1 = browser.find_element(By.XPATH, INPUTS[0])
        input2 = browser.find_element(By.XPATH, INPUTS[1])
        input3 = browser.find_element(By.XPATH, INPUTS[2])
    finally:
        sleep(5)
        browser.quit()

test1()
test2()


