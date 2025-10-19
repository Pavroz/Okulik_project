from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pytest

@pytest.fixture
def driver(request):
    options = Options()
    options.add_argument('start-maximized')
    driver = webdriver.Chrome(options=options)
    # driver.implicitly_wait(6)
    yield driver
    # sleep(3)

def test_clear(driver):
    input_data = 'test'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_string = driver.find_element(By.NAME, 'text_string')
    text_string.send_keys(input_data)
    # text_string.clear()
    entered_value = text_string.get_attribute('value')
    for _ in range(len(entered_value)):
        text_string.send_keys(Keys.BACKSPACE)
    assert text_string.is_displayed()

def test_enabled_and_selected(driver):
    driver.get('https://www.qa-practice.com/elements/button/disabled')
    button = driver.find_element(By.CSS_SELECTOR, 'input[name="submit"]')
    print(button.is_enabled())
    select = driver.find_element(By.ID, 'id_select_state')
    dropdown = Select(select)
    sleep(1)
    dropdown.select_by_value('enabled')
    sleep(1)
    print(button.is_enabled())

def test_5_sec(driver):
    driver.get('https://demoqa.com/dynamic-properties')
    button3 = driver.find_element(By.ID, 'visibleAfter')
    button3.click()

def test_cart(driver):
    driver.get('https://www.wildberries.ru/catalog/435659548/detail.aspx?size=618241927')
    wait = WebDriverWait(driver, 5)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[aria-label="Добавить в корзину"]')))
    button = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Добавить в корзину"]')
    button.click()
    # wait = WebDriverWait(driver, 5)
    # wait.until(EC.text_to_be_present_in_element_attribute())
    counter = driver.find_element(By.XPATH, '//span[@class="navbar-pc__notify"]')
    assert counter.text == '1'
    print(f'\n{counter.text}')
    driver.find_element(By.CSS_SELECTOR, 'a[data-wba-header-name="Cart"]').click()
    # Работа с куками
    driver.add_cookie({'name': 'test name', 'value': 'test value'})
    print(driver.get_cookies())

def test_5_sec2(driver):
    driver.get('https://demoqa.com/dynamic-properties')
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button#visibleAfter')))
    button3 = driver.find_element(By.CSS_SELECTOR, 'button#visibleAfter')
    button3.click()

# Взаимодействие с одинаковыми элементами на странице
def test_same_elements(driver):
    driver.get('https://www.wildberries.ru/')
    sleep(5)
    product_link = driver.find_elements(By.CSS_SELECTOR, '.main-page__product')
    print(len(product_link))
    print(product_link[0].text)
    print(product_link[-1].text)

def test_same_cards(driver):
    driver.get('https://www.wildberries.ru/')
    sleep(10)
    product_link = driver.find_elements(By.CSS_SELECTOR, '.main-page__product')
    for card in product_link:
        print(card.find_element(By.CSS_SELECTOR, '.price__lower-price').text)