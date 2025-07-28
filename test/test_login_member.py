import pytest
import time
from playwright.sync_api import sync_playwright
from pages.pages_login_member import LoginOneFlow  # Import the LoginOneFlow POM

@pytest.fixture(scope="function")
def setup_playwright():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, proxy={"server": "10.90.2.105:3128"})
        context = browser.new_context(base_url="https://staging-loyalty.bersama.id")
        request_context = context.request
        page = context.new_page()
        yield page, request_context
        browser.close()

def test_login_member(setup_playwright):
    page, request_context = setup_playwright
    login_page = LoginOneFlow(page, request_context)

    microsite_url = login_page.login_member("jazz.kvlar@gmail.com", "62876620760345", "Ajazz Kuvlar")
    print("Microsite URL:", microsite_url)
    time.sleep(2)
    page.screenshot(path="screenshots/test_login_member.png")

def test_login_aja(setup_playwright):
    page, request_context = setup_playwright
    login_page = LoginOneFlow(page, request_context)

    login_page.login_member_aja()
    time.sleep(2)
    page.screenshot(path="screenshots/test_login_aja.png")

