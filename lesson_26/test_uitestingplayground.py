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

    def test_progress_bar(self, page: Page, base_page, open):
        page.locator('a[href="/progressbar"]').click()
        start_button = page.locator('#startButton')
        stop_button = page.locator('#stopButton')
        progress_bar = page.locator('#progressBar')
        start_button.click()
        while True:
            text = progress_bar.inner_text() # inner_text() - получение текста из эелмента
            value = int(text.rstrip('%'))
            if value >= 75:
                stop_button.click()
                break

    def test_visibility(self, page: Page, base_page, open):
        page.locator('a[href="/visibility"]').click()
        page.locator("#hideButton").click()

        # Эти кнопки становятся НЕВИДИМЫМИ по критериям Playwright
        expect(page.locator("#removedButton")).not_to_be_attached()  # удалена из DOM
        expect(page.locator("#zeroWidthButton")).to_be_hidden()  # width: 0
        expect(page.locator("#invisibleButton")).to_be_hidden()  # visibility: hidden
        expect(page.locator("#notdisplayedButton")).to_be_hidden()  # display: none

        # Эти три — Playwright считает ВИДИМЫМИ (это и есть суть задания!)
        expect(page.locator("#transparentButton")).to_be_visible()  # opacity: 0
        expect(page.locator("#overlappedButton")).to_be_visible()  # перекрыта
        expect(page.locator("#offscreenButton")).to_be_visible()  # сдвинута влево на -100px
        
    def test_sample_app(self, page: Page, base_page, open):
        name = 'test'
        page.locator('a[href="/sampleapp"]').click()
        page.locator('input[name="UserName"]').fill(f'{name}')
        page.locator('input[name="Password"]').fill('pwd')
        page.locator('#login').click()
        expect(page.locator('#loginstatus')).to_have_text(f'Welcome, {name}!')
        page.get_by_text('Log Out').click()
        expect(page.locator('#loginstatus')).to_have_text('User logged out.')

    def test_mouse_over(self, page: Page, base_page, open):
        page.get_by_role('link', name='Mouse Over').click()
        page.locator('a[title="Click me"]').hover()
        page.locator('a[title="Active Link"]').click()
        page.locator('a[title="Active Link"]').click()
        expect(page.locator('#clickCount')).to_have_text('2')
        page.locator('a[title="Link Button"]').dblclick()
        expect(page.locator('#clickButtonCount')).to_have_text('2')

    def test_non_breaking_space(self, page: Page, base_page, open):
        page.get_by_role('link', name='Non-Breaking Space').click()
        page.get_by_role('button', name='My\u00A0Button').click()
        # \u00A0 - символ неразрывного пробела, если в html коде '&nbsp;'
        # Пример: <button class="btn btn-primary" type="button">My&nbsp;Button</button>