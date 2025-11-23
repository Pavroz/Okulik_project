from playwright.sync_api import Page, expect, sync_playwright


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto('http://uitestingplayground.com/')
