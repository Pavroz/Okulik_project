import re


from playwright.sync_api import Page, expect, sync_playwright
from time import sleep


# def test_one(page: Page):
#     page.goto('https://www.google.com/')
#     search_field = page.get_by_role('combobox')
#     search_field.fill('cat')
#     page.keyboard.press('Enter')
#     expect(page).to_have_title(re.compile('^cat'))

def test_first(page: Page):
    page.goto('http://arm-tablets.01-bfv-server.stroki.loc/auth') # Открытие страницы
    search_field = page.get_by_role('formcontrolname', name='login') # Поиск поля ввода по роли
    search_field.fill('cat') # Ввод в поле ввода значения
    sleep(2)
    search_field.press('Enter') # Нажатие ентера
    expect(page).to_have_title(re.compile('^cat')) # Проверка названия вкладки (^ - startswith, $ - endswith)

def test_by_text(page: Page):
    page.goto('https://www.saucedemo.com/')
    page.get_by_placeholder('Username').fill('standard_user')
    page.get_by_placeholder('Password').fill('secret_sauce')
    page.locator('#login-button').click()
    page.get_by_text('Sauce Labs Backpack').click()
    sleep(2)

def test_by_label():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel='chrome', headless=False,
                                    args=['--start-maximized', '--disable-cache', '--incognito'])
        # Создаём контекст (изолированная сессия, как incognito)
        context = browser.new_context(no_viewport=True)
        page = context.new_page()
        page.goto('https://ya.ru/')
        page.get_by_role('combobox').fill('Playwright')
        page.keyboard.press('Enter')
        sleep(5)
