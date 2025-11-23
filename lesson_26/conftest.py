import pytest
from playwright.sync_api import Page, expect, sync_playwright

from lesson_26.base_page import BasePage


@pytest.fixture(scope='function')
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel='chrome', headless=False,
                                    args=['--start-maximized', '--disable-cache', '--incognito'])
        # Создаём контекст (изолированная сессия, как incognito)
        context = browser.new_context(no_viewport=True)
        page = context.new_page()
        yield page
        context.close()
        browser.close()

@pytest.fixture(scope='function')
def open(page):
    page.goto('http://uitestingplayground.com/')

@pytest.fixture(scope='function')
def base_page(page):
    return BasePage(page)
