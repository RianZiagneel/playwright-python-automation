from playwright.sync_api import sync_playwright,expect
from pages.pages_dash_member import DashBoard
from test.test_bl_oneflow import test_bl_one_flow
import pytest


@pytest.mark.order(2)
def test_dashboard(page,request):
    page_dash = DashBoard(page)
    url_micro = test_bl_one_flow()
    page_dash.goto(url_micro)
    print("url_dash", url_micro)
    page.screenshot(path="screenshot_dash.png")

