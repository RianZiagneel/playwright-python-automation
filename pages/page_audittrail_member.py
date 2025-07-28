from pages.base_page import BasePage
from datetime import datetime

class AuditMemberPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        today = datetime.today().strftime("%B %d,").lstrip("0")
        self.m_audit_trail = self.page.get_by_role("link", name="nAudittrail Member").click()
        self.start_date = self.get_by_role("textbox", name="Select start date")
        self.end_date = self.get_by_role("textbox", name="Select end date")
        self.dropdown_opt = self.get_by_role("combobox").first
        self.type_opt_def = self.get_by_role("option", name="Default Type")
        self.type_opt_merchant = self.get_by_role("option", name="Merchant")
        self.type_opt_member = self.get_by_role("option", name="Member")
        self.dropdown_mod = self.get_by_role("combobox").nth(1)
        self.chart_bttn = self.get_by_text("Go To Chart")
        self.mod_opt_def = self.get_by_role("option", name="Default Module")
        self.mod_opt_dash = self.get_by_role("option", name="Dashboard")
        self.mod_opt_depo = self.get_by_role("option", name="Deposit")
        self.mod_opt_user = self.get_by_role("option", name="User")
        self.mod_opt_adv = self.get_by_role("option", name="Advertising")
        self.mod_opt_blast = self.get_by_role("option", name="Simply Blast")
        self.mod_opt_member = self.get_by_role("option", name="Member")
        self.mod_opt_tier = self.get_by_role("option", name="Tier")
        self.mod_opt_rule = self.get_by_role("option", name="Rules")
        self.mod_opt_promo = self.get_by_role("option", name="Promotion")
        self.mod_opt_prod = self.get_by_role("option", name="Product")
        self.mod_opt_reward = self.get_by_role("option", name="Reward")
        self.mod_opt_report = self.get_by_role("option", name="Report")
        self.mod_opt_point = self.get_by_role("option", name="Point Value")
        self.mod_opt_apprv = self.get_by_role("option", name="Approval")
        self.mod_opt_recon = self.get_by_role("option", name="Reconcile")
        self.mod_opt_audit = self.get_by_role("option", name="Audittrail")
        self.mod_opt_build = self.get_by_role("option", name="Builder")
        self.mod_opt_valid = self.get_by_role("option", name="Validation Voucher")
        self.clear_bttn = self.get_by_role("button", name="Clear Filters")
        self.adt_table_locator = self.page.locator("tr.ant-table-row")

    def get_date(self, date):
        return self.get_by_title(date).locator("div")
        