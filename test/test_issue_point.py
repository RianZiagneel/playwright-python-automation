import pytest
import time
import json
import uuid
from playwright.sync_api import sync_playwright, expect
from pages.pages_login_member import LoginOneFlow
from pages.page_report import  ReportPage
from pages.pages_login_merchant import LoginPage
from pages.page_dash_merchant import DashPage
from pages.pages_point_issue import PointIssue
from pages.pages_dash_member import DashBoard

@pytest.fixture(scope="function")

def setup_playwright():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, proxy={"server": "10.90.2.105:3128"})
        context = browser.new_context(base_url="https://staging-loyalty.bersama.id")
        request_context = context.request
        page = context.new_page()
        yield page, request_context
        browser.close()

def test_issue_point(setup_playwright):
    page, request_context = setup_playwright
    auth_token = LoginOneFlow(page,request_context).get_token()
    issue_page = PointIssue(page, request_context,auth_token)
    ref_id = str(uuid.uuid4())

    issue_point = issue_page.issue_point("Test_QA_AJ_2","BD0894D0-55B4-4313-B8E0-65E3BE2D8B35","DDC5520D-2340-4EC2-AAB6-279EF59984EE", ref_id,100000)

    print("Response Issue Point", json.dumps(issue_point))
    return ref_id

def test_report_issue(setup_playwright,normalize_number):
    page, request_context = setup_playwright

    login_merchant = LoginPage(page)
    dash = DashPage(page)
    report = ReportPage(page)
    auth_token = LoginOneFlow(page,request_context).get_token()
    
    issue = PointIssue(page, request_context,auth_token)
    issue_aja = issue.issue_point_aja()
    
    ref_id = issue_aja["refId"]
    tran_code = issue_aja["ruleName"]
    tran_amount = str(issue_aja["totalTrxAmount"])
    tran_poin = str(issue_aja["totalPointIssuing"])
    poin_deduc = str(issue_aja["pointFee"])
    time.sleep(10)

    login_merchant.loginaja()
    dash.reportbttn.click()

    time.sleep(2)
    report.point_report.click()
    page.keyboard.press("Home")
    print(issue_aja)
    time.sleep(2)
    page.screenshot(path= "screenshots/test_report_issue.png")
    expected_values = {
    1: "Ajazz Kuvlar",
    2: "jazz.kvlar@gmail.com",
    3: "62876620760345",
    4: ref_id,
    7: "Issuing",
    9: tran_code,
    10: tran_amount,
    11: tran_poin,
    12: poin_deduc
    }
    errors = []
    for col, expected_text in expected_values.items():
        actual_text = report.table_locator.first.locator(f"td:nth-child({col})").inner_text()
        print(type(actual_text))
        print(f"🔹 Column {col} | Expected ({type(expected_text)}): '{expected_text}' | Actual ({type(actual_text)}): '{actual_text}'")
        actual_text = normalize_number(actual_text)
        if actual_text != expected_text:
            errors.append(f"❌ Column {col}: Expected '{expected_text}', but got '{actual_text}'")

    if errors:
        print("\n".join(errors))
        assert False, "❌ Test failed due to mismatches"
    else:
        print("✅ All table values are correct!")

def test_claim_and_report(setup_playwright, normalize_number):
    page, request_context = setup_playwright
    login_merch = LoginPage(page)
    dash = DashPage(page)
    report = ReportPage(page)
    dash_member = DashBoard(page)
    login_page = LoginOneFlow(page, request_context)

    login_page.login_member_aja()
    dash_member.reward_bttn.click()
    dash_member.redeem_bttn.click()
    dash_member.yes_bttn.click()
    time.sleep(5)
    page.screenshot(path="screenshots/test_claim_and_report_1.png")
    time.sleep(20)
    login_merch.loginaja()
    dash.reportbttn.click()
    time.sleep(2)
    report.point_report.click()
    page.keyboard.press("Home")
    page.screenshot(path="screenshots/test_claim_and_report_2.png")

    expected_values = {
    1: "Ajazz Kuvlar",
    2: "jazz.kvlar@gmail.com",
    3: "62876620760345",
    # 4: ref_id,
    7: "Redeem",
    9: "TopedTestQA",
    # 10: tran_amount,
    11: "-5",
    12: "12"
    }
    errors = []
    for col, expected_text in expected_values.items():
        actual_text = report.table_locator.first.locator(f"td:nth-child({col})").inner_text()
        print(type(actual_text))
        print(f"🔹 Column {col} | Expected ({type(expected_text)}): '{expected_text}' | Actual ({type(actual_text)}): '{actual_text}'")
        actual_text = normalize_number(actual_text)
        if actual_text != expected_text:
            errors.append(f"❌ Column {col}: Expected '{expected_text}', but got '{actual_text}'")

    if errors:
        print("\n".join(errors))
        assert False, "❌ Test failed due to mismatches"
    else:
        print("✅ All table values are correct!")


    


    