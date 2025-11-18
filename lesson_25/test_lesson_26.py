import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

@pytest.fixture
def driver(request):
    options = Options()
    options.add_argument('start-maximized')
    driver = webdriver.Chrome(options=options)
    yield driver
    sleep(3)


# Прокрутка до конца страницы
def test_scroll(driver):
    driver.get('https://www.onliner.by/')
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Скролл к конкретному элементу
def test_scroll_to_element(driver):
    driver.get('https://www.onliner.by/')
    link = driver.find_element(By.XPATH, '(//a[text()="Технологии"])[3]')
    driver.execute_script('arguments[0].scrollIntoView();', link)

# Загрузка файлов с пк
def test_upload(driver):
    driver.get('https://the-internet.herokuapp.com/upload')
    upload = driver.find_element(By.ID, 'file-upload')
    button = driver.find_element(By.ID, 'file-submit')
    upload.send_keys('C:/270.jpg')
    sleep(3)
    button.click()
