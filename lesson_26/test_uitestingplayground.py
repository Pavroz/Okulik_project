import re
from playwright.sync_api import Page, expect, sync_playwright
from time import sleep
from lesson_26.base_page import BasePage


class TestUi:


    def test_ajax_data(self, page: Page, base_page, open):
        page.locator('a[href="/ajax"]').click()
        page.locator('#ajaxButton').click()
        page.locator('//p[text()="Data loaded with AJAX get request."]').wait_for(state='visible')

    def test_click(self, page: Page, base_page, open):
        page.locator('a[href="/click"]').click()
        button = page.locator('#badButton')
        expect(button).to_have_class('btn btn-primary')
        button.click()
        expect(button).to_have_class('btn btn-success')

    def test_text_input(self, page: Page, base_page, open):
        page.locator('a[href="/textinput"]').click()
        field = page.get_by_label('Set New Button Name')
        button = page.locator('#updatingButton')
        expect(button).to_have_text("Button That Should Change it's Name Based on Input Value")
        field.fill('Test')
        button.click()
        expect(button).to_have_text('Test')

    def test_scrollbar(self, page: Page, base_page, open):
        page.locator('a[href="/scrollbars"]').click()
        delta_x = 300 # Горизонталь вправо
        delta_y = 150 # Вертикаль вниз
        duration = 1.5 # За какое время происходит один скролл
        steps = 30 # Количество пикселей, на которые происходит движение
        container = page.locator('//div[@style="height:150px;overflow-y: scroll;width:300px;overflow-x:scroll"]')
        container.hover() # Наведение курсона мыши на контейнер со скроллом
        delay = duration / steps # Пауза между шагами (0.05 сек)
        step_x = delta_x // steps # Каждый шаг по X = 10px
        step_y = delta_y // steps # Каждый шаг по Y = 5px
        for _ in range(steps):
            page.mouse.wheel(step_x, step_y) # Маленькое движение колесика (10, 5)
            sleep(delay) # Ждем 0.05 сек, получается плавные движение
        page.mouse.wheel(delta_x % steps, delta_y % steps) # Последний шаг — добивает остаток (300 % 30 = 0, 150 % 30 = 0 → ничего)
        page.locator('#hidingButton').click()

    def test_dynamic_table(self, page: Page, open):
        page.locator('a[href="/dynamictable"]').click()
        expected = page.locator('.bg-warning').text_content().split()[-1]
        actual = (page.get_by_role('row', name=re.compile(r'Chrome'))
                  .get_by_role('cell', name=re.compile(r'%$')).text_content())
        assert actual == expected

    def test_verify_text(self, page: Page, base_page, open):
        # text = page.get_by_text(re.compile(r'Welcome'))
        page.locator('a[href="/verifytext"]').click()
        # text = 'Welcome'
        expect(page.get_by_text("Welcome", exact=True)).to_be_hidden()