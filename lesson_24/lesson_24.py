from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pytest

@pytest.fixture
def driver():
    options = Options()
    options.add_argument('start-maximized')
    driver = webdriver.Chrome(options=options)
    # sleep(1)
    yield driver
#     sleep(1)


def test_new_tab(driver):
    driver.get('https://demoqa.com/browser-windows')
    driver.find_element(By.ID, 'tabButton').click()
    tabs = driver.window_handles # Получение списка вкладов
    driver.switch_to.window(tabs[1]) # Переключение на вторую вкладку
    result = driver.find_element((By.ID, 'sampleHeading'))
    print(result)
    sleep(2)
    # assert result.text == 'This is a sample page'

def test_stale_exception(driver):
    driver.get('https://demoqa.com/checkbox')
    checkbox = driver.find_element(By.CSS_SELECTOR, '.rct-checkbox')
    checkbox.click()
    text_result = driver.find_elements(By.CSS_SELECTOR, '.text-success')
    list_result = []
    for i in text_result:
        list_result.append(i.text)
    result = ', '.join(list_result)
    print(result)
    assert result == 'home, desktop, notes, commands, documents, workspace, react, angular, veu, office, public, private, classified, general, downloads, wordFile, excelFile'
    print('Все заебись!')

def test_iframe(driver):
    driver.get('https://demoqa.com/frames')
    iframe = driver.find_element(By.ID, 'frame2')
    driver.switch_to.frame(iframe)

# Наведение на элемент в дропдауне
def test_drop_menu(driver):
    driver.get('https://html-plus.in.ua/css-dropdown-menu-examples/')
    js = driver.find_element(By.ID, 'menu-item-361')
    os = driver.find_element(By.XPATH, '//li[@id="menu-item-361"]//a[text()="Обработка событий"]')
    actions = ActionChains(driver)
    actions.move_to_element(js)
    sleep(1)
    actions.click(os)
    sleep(1)
    actions.perform()
    sleep(3)

def test_dnd(driver):
    driver.get('https://demoqa.com/dragabble')
    first = driver.find_element(By.ID, 'dragBox')
    second = driver.find_element(By.ID, 'Ad.Plus-970x250-2')
    actions = ActionChains(driver)
    actions.drag_and_drop(first, second)
    actions.perform()
    sleep(1)
    ## Второй вариант реализации
    # actions.click_and_hold(first)
    # actions.move_to_element(second)
    # actions.release()
    # actions.perform()

def test_open_in_new_tab(driver):
    driver.get('https://demoqa.com/')
    link = driver.find_element(By.CSS_SELECTOR, 'a[href="https://demoqa.com"]')
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()
    sleep(2)

def test_alerts(driver):
    driver.get('https://demoqa.com/alerts')
    driver.find_element(By.ID, 'alertButton').click()
    sleep(1)
    alert = Alert(driver)
    alert.accept()
    sleep(1)