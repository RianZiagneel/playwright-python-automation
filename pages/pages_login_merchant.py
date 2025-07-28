from pages.base_page import BasePage
from datetime import datetime
import time
class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        #page login
        self.username_input = self.get_by_placeholder("Email")
        self.password_input = self.get_by_placeholder("Password")
        self.loginbttn = self.get_by_role("button", name="Login")  
        self.captcha = self.page.locator(".recaptcha-checkbox")
        self.captcha_verify_bttn = self.page.locator("iframe[name=\"c-pyaehtetvfms\"]").content_frame.get_by_role("button", name="Verify")
        self.chart_promotion = self.get_by_role("main").get_by_text("Promotion", exact=True)
        self.welcome_back = self.get_by_text("Hello,Welcome Back")

        #forgot pass
        self.forgotpass = self.get_by_role("button", name="Forgot Password")
        self.enter_email = self.get_by_placeholder("Email Address")
        self.sendbttn = self.get_by_role("button", name="SEND")
        self.okbttn = self.get_by_role("button", name="OK")
        self.back_bttn = self.get_by_role("button", name="Back")

        self.timestamp = None

    def login(self, username: str, password: str, item):
        test_case = item.name
        self.goto("https://staging-loyalty.bersama.id/signin")
        self.fill(self.username_input, username)
        self.fill(self.password_input, password)
        
        self.page.screenshot(path=f"screenshots/{test_case}_1.png")
        time.sleep(5)
        self.loginbttn.click()
        if self.timestamp is None:
            self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        

    def loginaja(self,item):
        test_case = item.name
        self.goto("https://staging-loyalty.bersama.id/signin")
        self.fill(self.username_input, "bimaranggawisnu92@gmail.com")
        self.fill(self.password_input, "L0y4ltyAjBrKs!")
        self.page.screenshot(path=f"screenshots/{test_case}_1.png")
        self.click(self.loginbttn)
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def buttonlogin(self):
        self.click(self.loginbttn)

    def loginCaptcha(self, username: str, password: str):
        with recaptchav2.SyncSolver(BasePage) as solver:    
            self.goto("https://staging-loyalty.bersama.id/")
            self.fill(self.username_input, username)
            self.fill(self.password_input, password)
            # self.click(self.captcha)
            solver.solve_recaptcha
            self.page.screenshot(path="screenshots/loginPage.png")    


