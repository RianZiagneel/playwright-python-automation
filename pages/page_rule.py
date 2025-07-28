from pages.base_page import BasePage
import time

class RulePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.rulebttn = self.get_by_role("link", name="Rules")
        self.rule_list = self.get_by_text("Rule ListReview and edit your")
        self.search_rule = self.get_by_placeholder("Search rules by name")
        self.create_basic_rule = self.get_by_role("heading", name="Create Basic Rule")
        self.create_reff_rule = self.get_by_role("heading", name="Create Refferal Rule")
        self.create_cust_rule = self.get_by_role("heading", name="Create Custom Rule")
        # Edit Rule
        self.filter_rule_name = self.get_by_role("button", name="Test_QA_AJ_2")
        self.backbttn = self.get_by_role("button", name="Back")
        self.editbttn =  self.get_by_role("button", name="Edit")
        self.rule_name = self.get_by_placeholder("Rule Name")
        self.rule_desc = self.get_by_placeholder("Rule Description")
        self.base_point = self.get_by_label("Base Loyalty Point")
        self.option_amount = self.locator("#customRuleType div")
        self.opt_fix_amount = self.get_by_role("option", name="Fixed Amount")
        self.opt_perc_amount = self.get_by_role("option", name="Percentage Amount")
        self.for_each_amount = self.get_by_label("For Each Amount Of (Rp)")
        self.base_disc = self.get_by_label("Base Loyalty Discount(%)")
        self.max_point = self.get_by_label("Maximum Points")
        self.submitbttn = self.get_by_role("button", name="Submit")

        # 