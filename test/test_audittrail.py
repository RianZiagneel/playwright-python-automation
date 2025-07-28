import time
import json
import uuid
from datetime import datetime, timedelta
from pages.pages_login_member import LoginOneFlow
from pages.page_report import  ReportPage
from pages.pages_login_merchant import LoginPage
from pages.page_dash_merchant import DashPage
from pages.pages_point_issue import PointIssue
from pages.pages_dash_member import DashBoard
from pages.page_audittrail import AuditPage
from pages.page_rule import RulePage
from pages.page_promotion import PromoPage
from pages.pages_product import ProductPage
from dateutil.relativedelta import relativedelta

def test_adt_0001(page,check_expectation,request):

    login_page = LoginPage(page)
    audit_page = AuditPage(page)
    login_page.loginaja(request.node)
    audit_page.m_audit_trail.click()
    page.screenshot(path="screenshots/test_adt_0001_2.png")
    time.sleep(3)
    check_expectation(page,"Start Date", audit_page.start_date, check_visibility=True)
    check_expectation(page,"End Date", audit_page.end_date, check_visibility=True)
    check_expectation(page,"Default Type", audit_page.dropdown_opt, check_visibility=True)
    check_expectation(page,"Default Module", audit_page.dropdown_mod, check_visibility=True)
    check_expectation(page,"Clear Filter", audit_page.clear_bttn, check_visibility=True)
    check_expectation(page,"Go To Chart", audit_page.chart_bttn, check_visibility=True)

    
    

def test_adt_0002(page, request):
    login_page = LoginPage(page)
    audit_page = AuditPage(page)
    login_page.loginaja(request.node)
    timestamp = login_page.timestamp
    audit_page.m_audit_trail.click()
    page.screenshot(path="screenshots/test_adt_0002_2.png")
    audit_table = audit_page.adt_table_locator
    
    
    expected_values = {
    1: "127.0.0.1",  # IP Address
    2: timestamp,  # Timestamp
    3: "User",  # Module Name
    4: "User Login",  # Action
    5: "bimaranggawisnu92@gmail.com",  # Email
    6: "Success",  # Status
    9: "loginName: bimaranggawisnu92@gmail.com"  # After Status Change
}
    errors = []
    for col, expected_text in expected_values.items():
        actual_text = audit_table.first.locator(f"td:nth-child({col})").inner_text()
        print(type(actual_text))
        print(f"🔹 Column {col} | Expected ({type(expected_text)}): '{expected_text}' | Actual ({type(actual_text)}): '{actual_text}'")
        if actual_text != expected_text:
            errors.append(f"❌ Column {col}: Expected '{expected_text}', but got '{actual_text}'")

    if errors:
        print("\n".join(errors))
        assert False, "❌ Test failed due to mismatches"
    else:
        print("✅ All table values are correct!")

def test_adt_0003(page,request):
    login_page = LoginPage(page)
    audit_page = AuditPage(page)
    today = datetime.today().strftime("%B %#d, %Y").lstrip("0")
    login_page.loginaja(request.node)
    audit_page.m_audit_trail.click()
    audit_page.start_date.click()
    page.screenshot(path="screenshots/test_adt_0003_2.png")
    audit_page.get_date(today).click()
    time.sleep(2)
    page.screenshot(path="screenshots/test_adt_0003_3.png")

def test_adt_0004(page,request):
    login_page = LoginPage(page)
    audit_page = AuditPage(page)
    yesterday =  (datetime.today() - timedelta(days=1)).strftime("%B %#d, %Y")
    login_page.loginaja(request.node)
    audit_table = audit_page.adt_table_locator
    audit_page.m_audit_trail.click()
    audit_page.end_date.click()
    page.screenshot(path="screenshots/test_adt_0004_2.png")
    audit_page.get_date(yesterday).click()
    time.sleep(2)
    page.screenshot(path="screenshots/test_adt_0004_3.png")

    expected_values = {
    1: "127.0.0.1",  # IP Address
    3: "User",  # Module Name
    4: "User Login",  # Action
    5: "bimaranggawisnu92@gmail.com",  # Email
    6: "Success",  # Status
    9: "loginName: bimaranggawisnu92@gmail.com"  # After Status Change
}
    errors = []
    for col, expected_text in expected_values.items():
        actual_text = audit_table.first.locator(f"td:nth-child({col})").inner_text()
        print(type(actual_text))
        print(f"🔹 Column {col} | Expected ({type(expected_text)}): '{expected_text}' | Actual ({type(actual_text)}): '{actual_text}'")
        if actual_text != expected_text:
            errors.append(f"❌ Column {col}: Expected '{expected_text}', but got '{actual_text}'")

    if errors:
        print("\n".join(errors))
        assert False, "❌ Test failed due to mismatches"
    else:
        print("✅ All table values are correct!")

def test_adt_0005(page, request,check_expectation):
    login_page = LoginPage(page)
    audit_page = AuditPage(page)
    today = datetime.today().strftime("%B %#d, %Y").lstrip("0")
    yesterday =  (datetime.today() - timedelta(days=1)).strftime("%B %#d, %Y")
    login_page.loginaja(request.node)
    audit_page.m_audit_trail.click()
    check_expectation(page,"Start Date", audit_page.start_date, check_visibility=True)
    check_expectation(page,"End Date", audit_page.end_date, check_visibility=True)
    audit_page.start_date.click()
    page.screenshot(path="screenshots/test_adt_0005_2.png")
    audit_page.get_date(yesterday).click()
    audit_page.end_date.click()
    page.screenshot(path="screenshots/test_adt_0005_3.png")
    audit_page.get_date(today).click()
    time.sleep(2)
    page.screenshot(path="screenshots/test_adt_0005_4.png")

def test_adt_0006(page, request,check_expectation):
    login_page = LoginPage(page)
    audit_page = AuditPage(page)
    login_page.loginaja(request.node)
    audit_page.m_audit_trail.click()
    time.sleep(2)
    check_expectation(page,"Default Type", audit_page.dropdown_opt, check_visibility=True)
    check_expectation(page,"Default Module", audit_page.dropdown_mod, check_visibility=True)
    audit_page.dropdown_opt.click()
    audit_page.type_opt_def.click()
    page.screenshot(path="screenshots/test_adt_0006_2.png")
    audit_page.dropdown_mod.click()
    audit_page.mod_opt_def.click()
    page.screenshot(path="screenshots/test_adt_0006_3.png")

def test_adt_0007(page, request,check_expectation):
    login_page = LoginPage(page)
    audit_page = AuditPage(page)
    login_page.loginaja(request.node)
    audit_page.m_audit_trail.click()
    time.sleep(2)
    check_expectation(page,"Default Type", audit_page.dropdown_opt, check_visibility=True)
    check_expectation(page,"Default Module", audit_page.dropdown_mod, check_visibility=True)
    audit_page.dropdown_opt.click()
    audit_page.type_opt_merchant.click()
    time.sleep(3)
    page.screenshot(path="screenshots/test_adt_0007_2.png")
    audit_page.dropdown_mod.click()
    audit_page.mod_opt_user.click()
    time.sleep(3)
    page.screenshot(path="screenshots/test_adt_0007_3.png")

def test_adt_0008(page, request,check_expectation):
    login_page = LoginPage(page)
    audit_page = AuditPage(page)
    promo_page = PromoPage(page)
    today = datetime.today().strftime("%B %#d, %Y").lstrip("0")
    next_month =  (datetime.today() + relativedelta(months=1)).strftime("%B %#d, %Y")
    login_page.loginaja(request.node)
    
    add_rule = ["Test_QA_AJ_2","rule1","Rule_Test_QA"]

    promo_page.create_promotion("TEST QA AJ BRKS 3","TEST QA AJ BRKS 3","TEST QA AJ BRKS 3",today,next_month,add_rule,request.node)
    audit_page.m_audit_trail.click()
    page.keyboard.press("Home")
    time.sleep(3)
    audit_page.start_date.scroll_into_view_if_needed()
    page.screenshot(path="screenshots/test_adt_0008_audit.png")

def test_adt_0009(page, request, check_expectation):
    login_page = LoginPage(page)
    audit_page = AuditPage(page)
    promo_page = PromoPage(page)
    today = datetime.today().strftime("%B %#d, %Y").lstrip("0")
    next_month =  (datetime.today() + relativedelta(months=1)).strftime("%B %#d, %Y")
    next_week =  (datetime.today() + relativedelta(days=1)).strftime("%B %#d, %Y")
    login_page.loginaja(request.node)
    promo_page.promo_bttn.click()
    promo_page.promo_list.click()
    promo_page.promo_search.fill("TEST QA AJ BRKS 2")
    page.keyboard.press("Enter")
    page.screenshot(path="screenshots/test_adt_0009_2.png")
    
    promo_page.edit_bttn.click()
    promo_page.promo_code.fill("Test QA 2 EDIT")
    promo_page.promo_name_fill.fill("Test QA 2 EDIT")
    promo_page.promo_desc.fill("Test QA 2 EDIT")
    page.screenshot(path="screenshots/test_adt_0009_3.png")
    promo_page.submit_bttn.click()
    time.sleep(3)
    page.screenshot(path="screenshots/test_adt_0009_4.png")
    promo_page.ok_bbtn.click()
    
    audit_page.m_audit_trail.click()
    audit_page.start_date.scroll_into_view_if_needed()
    page.screenshot(path="screenshots/test_adt_0009_audit.png")


def test_adt_0010(page, request, check_expectation):
    login_page = LoginPage(page)
    audit_page = AuditPage(page)
    promo_page = PromoPage(page)
    login_page.loginaja(request.node)
    promo_page.promo_bttn.click()
    promo_page.promo_list.click()
    promo_page.promo_search.fill("TEST QA AJ BRKS 2")
    page.keyboard.press("Enter")
    page.screenshot(path="screenshots/test_adt_0010_2.png")
    if promo_page.active_bbtn.is_visible():
       promo_page.active_bbtn.click()
    elif promo_page.inactive_bbtn.is_visible():
       promo_page.inactive_bbtn.click()
    else: print("❌ Neither 'Active' nor 'Inactive' button is present")
    page.screenshot(path="screenshots/test_adt_0010_3.png")
    promo_page.update_bttn.click()
    time.sleep(2)
    page.screenshot(path="screenshots/test_adt_0010_4.png")
    promo_page.ok_bbtn.click()
    promo_page.promo_search.fill("TEST QA AJ BRKS 2")
    page.keyboard.press("Enter")
    page.screenshot(path="screenshots/test_adt_0010_5.png")
    audit_page.m_audit_trail.click()
    audit_page.start_date.scroll_into_view_if_needed()
    page.screenshot(path="screenshots/test_adt_0010_audit.png")


def test_adt_0011(page, request, check_expectation): #manual test for success create product
    login_page = LoginPage(page)
    audit_page = AuditPage(page)
    product_page = ProductPage(page)
    login_page.loginaja(request.node)
    product_page.m_prod_page.click()
    product_page.voucher.click()
    page.screenshot(path="screenshots/test_adt_0011_2.png")
    time.sleep(2)
    product_page.product_code.click()
    product_page.product_code.fill("Test QA AJ BRKS")
    product_page.product_name.fill("Test QA AJ BRKS")
    # product_page.product_desc_html.click()
    product_page.product_desc_body.fill("Test QA AJ BRKS 12")
    # product_page.paragraph_fill.fill("Test AJA")
    time.sleep(3)
    page.screenshot(path="screenshots/test_adt_0011_3.png")
    product_page.product_show_merchant.click()
    product_page.product_submit_list.click()
    time.sleep(2)
    # product_page.product_image_upload.click()
    page.screenshot(path="screenshots/test_adt_0011_4.png")
    # Locate the hidden file input inside the uploader and upload a file
    product_page.product_image_upload.scroll_into_view_if_needed()
    page.locator("input[type='file']").set_input_files("picture/product_icon_bl.jpg")

    # product_page.product_image_upload.set_input_files("picture/product_icon_bl.jpg")
    page.screenshot(path="screenshots/test_adt_0011_5.png")
    product_page.product_base_price.fill("10")
    product_page.product_submit_bttn.click()
    time.sleep(3)
    page.screenshot(path="screenshots/test_adt_0011_6.png")


def test_adt_0012(page, request, check_expectation): 
    login_page = LoginPage(page)
    audit_page = AuditPage(page)
    product_page = ProductPage(page)
    login_page.loginaja(request.node)
    product_page.m_prod_page.click()
    product_page.product_list.click()
    product_page.search_product.fill("Test 123")
    page.screenshot(path="screenshots/test_adt_0012_2.png")
    page.keyboard.press("Enter")
    product_page.edit_bttn.click()
    product_page.product_name.fill("Test 123 Automation")
    page.screenshot(path="screenshots/test_adt_0012_3.png")
    product_page.product_submit_bttn.click()
    page.screenshot(path="screenshots/test_adt_0012_4.png")
    product_page.ok_bttn.click()
    audit_page.m_audit_trail.click()
    page.screenshot(path="screenshots/test_adt_0012_5.png")

def test_adt_0013(page, request, check_expectation): 
    login_page = LoginPage(page)
    audit_page = AuditPage(page)
    product_page = ProductPage(page)
    next_month =  (datetime.today() + relativedelta(months=1)).strftime("%B %#d, %Y")
    next_week =  (datetime.today() + relativedelta(days=7)).strftime("%B %#d, %Y")
    login_page.loginaja(request.node)
    product_page.m_prod_page.click()
    product_page.product_list.click()
    product_page.search_product.fill("Test 123")
    page.keyboard.press("Enter")
    page.screenshot(path="screenshots/test_adt_0013_2.png")
    product_page.add_stock_bttn.click()
    page.screenshot(path="screenshots/test_adt_0013_3.png")
    product_page.generate_voucher.click()
    product_page.select_date.click()
    product_page.get_date(next_week).click()
    product_page.add_stock.fill("5")
    page.screenshot(path="screenshots/test_adt_0013_4.png")
    product_page.gen_bttn.click()
    page.screenshot(path="screenshots/test_adt_0013_5.png")
    product_page.save_bttn.click()
    product_page.ok_bttn.click()
    page.screenshot(path="screenshots/test_adt_0013_6.png")
    audit_page.m_audit_trail.click()
    page.screenshot(path="screenshots/test_adt_0013_7.png")

def test_adt_0014(page, request, check_expectation): 
    login_page = LoginPage(page)
    audit_page = AuditPage(page)
    product_page = ProductPage(page)
    next_month =  (datetime.today() + relativedelta(months=1)).strftime("%B %#d, %Y")
    next_week =  (datetime.today() + relativedelta(days=7)).strftime("%B %#d, %Y")
    login_page.loginaja(request.node)
    product_page.m_prod_page.click()
    product_page.product_list.click()
    page.screenshot(path="screenshots/test_adt_0014_2.png")
    product_page.search_product.fill("AJBRKS")
    page.keyboard.press("Enter")
    page.screenshot(path="screenshots/test_adt_0014_3.png")
    product_page.delete_bttn.click()
    page.screenshot(path="screenshots/test_adt_0014_4.png")
    product_page.yes_bttn.click()
    page.screenshot(path="screenshots/test_adt_0014_5.png")
    product_page.ok_bttn.click()
    page.screenshot(path="screenshots/test_adt_0014_6.png")
    audit_page.m_audit_trail.click()
    page.screenshot(path="screenshots/test_adt_0014_7.png")














