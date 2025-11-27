class LoaderPage:
    def __init__(self,page):
        self.page = page
        self.start_btn = 'button:has-text("start")'
        self.hello_msg = 'h4:has-text("Hello World!")'
    def nav(self):
        self.page.goto('https://the-internet.herokuapp.com/dynamic_loading/1')
    def startt(self):
        self.page.locator(self.start_btn).wait_for()
        self.page.locator(self.start_btn).click()
    def get_finished_text(self):
        self.page.locator(self.hello_msg).wait_for()
        return self.page.locator(self.hello_msg).inner_text()
