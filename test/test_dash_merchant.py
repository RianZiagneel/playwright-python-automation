import pytest_html.extras
from pages.base_page import BasePage

import time
import pytest_html
from pages.pages_login_merchant import LoginPage
from pages.page_dash_merchant import DashPage

def test_dash_merchant(page,check_expectation):
    login = LoginPage(page)
    dash_page = DashPage(page)
    login.loginaja()
    time.sleep(5)
    # check_expectation("Dashboard Chart", dash_page.chartdash, is_visible=True)
    page.screenshot(path="screenshots/test_dash_merchant.png")

def test_log_out(page,check_expectation):
    login = LoginPage(page)
    dash_page = DashPage(page)
    login.loginaja()
    time.sleep(2)
    dash_page.usermenu.click()
    page.screenshot(path="screenshots/test_log_out_1.png")
    dash_page.logoutbttn.click()
    check_expectation("Hello", login.welcome_back, is_visible=True)
    page.screenshot(path="screenshots/test_log_out_2.png")

    
