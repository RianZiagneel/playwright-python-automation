import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import time
import pytest
import json
import uuid
from playwright.sync_api import sync_playwright
from datetime import datetime, timedelta
from pages.pages_login_member import LoginOneFlow
from pages.pages_login_merchant import LoginPage
from pages.page_report import  ReportPage
from pages.page_audittrail_member import AuditMemberPage
from dateutil.relativedelta import relativedelta

@pytest.fixture(scope="function")
def setup_playwright():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, proxy={"server": "10.90.2.105:3128"})
        context = browser.new_context(base_url="https://staging-loyalty.bersama.id")
        request_context = context.request
        # page = context.new_page()
        yield request_context
        browser.close()

def test_adr_0001(page,check_expectation, request, setup_playwright):
    request_context = setup_playwright
    login_member = LoginOneFlow(page, request_context)
    login_merchant = LoginPage(page)
    audit_member = AuditMemberPage(page)

    login_member.login_member_aja()
    page.screenshot(path="screenshots/test_adr_0001_2.png")
    login_merchant.loginaja(request.node)
    audit_member.m_audit_trail.click()

    page.screenshot(path="screenshots/test_adr_0001_3.png")
    time.sleep(3)


