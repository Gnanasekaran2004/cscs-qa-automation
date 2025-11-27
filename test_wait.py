from pages.loader_page import LoaderPage
from playwright.sync_api import sync_playwright

def test_wait():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False,slow_mo=1000)
        page = browser.new_page()

        loader = LoaderPage(page)

        loader.nav()

        loader.startt()

        hello_text = loader.get_finished_text()
        assert "Hello World!" in hello_text,"Error in the result"
