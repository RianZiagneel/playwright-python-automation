from pages.base_page import BasePage
from playwright.sync_api import sync_playwright,expect
import time
from pages.pages_login_merchant import LoginPage
from pages.page_dash_merchant import DashPage


def test_login_success(page,check_expectation, request):
    page_login = LoginPage(page)
    dash_page = DashPage(page)
    # stealth_sync(page)
    page_login.login("bimaranggawisnu92@gmail.com","L0y4ltyAjBrKs!",request.node)
    page.screenshot(path="screenshots/test_login_success_2.png")
    time.sleep(5)
    # check_expectation("Promotion", dash_page.chartdash, is_visible=True)
    page.screenshot(path="screenshots/test_login_success_3.png")

    
    page.close()

def test_login_failed(page,request):
    failed_login = LoginPage(page)
    failed_login.login("test_salah_user","salah_pass", request.node)
    page.screenshot(path="screenshots/test_login_failed_2.png")
    page.close()

def test_forgot_pass(page):
    forgot_pass = LoginPage(page)
    forgot_pass.goto("https://staging-loyalty.bersama.id/")
    forgot_pass.forgotpass.click()
    page.screenshot(path="screenshots/test_forgot_pass_1.png")
    forgot_pass.enter_email.fill("ghazian.syazili@artajasa.co.id")
    time.sleep(5)
    page.screenshot(path="screenshots/test_forgot_pass_2.png")
    forgot_pass.sendbttn.click()
    time.sleep(2)
    page.screenshot(path="screenshots/test_forgot_pass_3.png")
    forgot_pass.okbttn.click()
    forgot_pass.back_bttn.click()
    page.close()

def test_user_profile(page, check_expectation,request):
    user_profile = LoginPage(page)
    user_dash = DashPage(page)
    user_profile.login("bimaranggawisnu92@gmail.com", "L0y4ltyAjBrKs!",request.node)
    time.sleep(3)
    page.screenshot(path="screenshots/test_user_profile_2.png")
    # check_expectation("Promotion", dash_page.chartdash, is_visible=True)
    user_dash.usermenu.click()
    page.screenshot(path="screenshots/test_user_profile_3.png")
    user_dash.usercontact.click()
    check_expectation("User Contact Page", user_dash.contact, is_visible=True)
    check_expectation("Profile Name", user_dash.profile_name, "UAT BRKS -")
    check_expectation("Profile Email", user_dash.profile_email, "bimaranggawisnu92@gmail.com")
    check_expectation("Profile Phone", user_dash.profile_phone, "081382317902")
    page.screenshot(path="screenshots/test_user_profile_4.png")

def test_user_profile_user_lain(page, check_expectation,request):
    user_profile = LoginPage(page)
    user_dash = DashPage(page)
    user_profile.login("bl.admin2@mailinator.com", "Adm!n_password2022",request.node)
    time.sleep(3)
    page.screenshot(path="screenshots/test_user_profile_user_lain_2.png")
    # check_expectation("Promotion", dash_page.chartdash, is_visible=True)
    user_dash.usermenu.click()
    page.screenshot(path="screenshots/test_user_profile_user_lain_3.png")
    user_dash.usercontact.click()
    check_expectation("User Contact Page", user_dash.contact, is_visible=True)
    check_expectation("Profile Name", user_dash.profile_name, "Admin Bersama -")
    check_expectation("Profile Email", user_dash.profile_email, "bl.admin2@mailinator.com")
    check_expectation("Profile Phone", user_dash.profile_phone, "62806222103499")
    page.screenshot(path="screenshots/test_user_profile_user_lain_4.png")


