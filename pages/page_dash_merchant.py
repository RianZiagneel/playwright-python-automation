from pages.base_page import BasePage

import time

class DashPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        #define button/link
        self.promotion = self.get_by_role("main").get_by_text("Promotion", exact=True)
        self.dashbttn = self.get_by_role("link", name="/Dashboard")
        self.depobttn = self.get_by_role("link", name="Deposit")
        self.userbttn = self.get_by_role("link", name="User")
        self.userlist = self.get_by_role("heading", name="User List")
        self.auditbttn = self.get_by_role("link", name="nAudittrail")
        self.voucherbttn = self.get_by_role("link", name="Validation Voucher")
        self.adverbttn = self.get_by_role("link", name="Advertising")
        self.blastbttn = self.get_by_role("link", name="Simply Blast")
        self.memberbttn = self.get_by_role("link", name="Member")
        self.tierbttn = self.get_by_role("link", name="Tier")
        self.rulebttn = self.get_by_role("link", name="Rules")
        self.promobttn = self.get_by_role("link", name="Promotion")
        self.prodbttn = self.get_by_role("link", name="Product")
        self.rewardbttn = self.get_by_role("link", name="Reward")
        self.reportbttn = self.get_by_role("link", name="NReport")
        self.pointvalue = self.get_by_role("link", name="AvatarPoint Value")
        self.approval = self.get_by_role("link", name="AvatarApproval")
        self.reconbttn = self.get_by_role("link", name="AvatarReconcile")
        self.chartdash =  self.get_by_text("Promotion")
        #menu log out
        self.usermenu = self.page.locator(".gx-avatar-name > .icon")
        self.usercontact = self.page.get_by_text("User Contact")
        self.accountbttn = self.page.get_by_text("My Account")
        self.changepass = self.page.get_by_text("Change Password")
        self.logoutbttn = self.page.get_by_text("Logout")
        # user profile
        self.contact = self.page.locator('div.ant-card-head-title:has-text("Contact")')
        self.profile_name = self.page.locator("//div[@class='gx-media-body']//span[text()='Name']/following-sibling::p")
        self.profile_email = self.page.locator("//div[@class='gx-media-body']//span[text()='Email']/following-sibling::p")
        self.profile_phone = self.page.locator("//div[@class='gx-media-body']//span[text()='Phone Number']/following-sibling::p")