from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import pytest

# @pytest.fixture
# def driver(request):
#     options = Options()
#     options.add_argument('start-maximized')
#     driver = webdriver.Chrome(options=options)
#     yield driver
#     sleep(3)
#
# def test_id_name(driver):
#     input_data = 'test'
#     driver.get('https://www.qa-practice.com/elements/input/simple')
#     text_string = driver.find_element(By.ID, 'id_text_string')
#     text_string.send_keys(input_data)
#     text_string.send_keys(Keys.ENTER)
#     result_text = driver.find_element(By.ID, 'result-text')
#     assert result_text.text == input_data
#
# def test_css_selector(driver):
#     input_data = 'test'
#     driver.get('https://www.qa-practice.com/elements/input/simple')
#     text_string = driver.find_element(By.CSS_SELECTOR, '[placeholder="Submit me"]')
#     text_string.send_keys(input_data)
#     text_string.send_keys(Keys.ENTER)
#     assert text_string.get_attribute('placeholder') == 'Submit me'