from pages.base_page import BasePage

import time

class PromoPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        #define button/link
        self.promo_bttn = self.get_by_role("link", name="Promotion")
        self.promo_list = self.get_by_role("heading", name="Promotion List")
        self.promo_search = self.get_by_placeholder("Search promotions by name")
        self.clear_bttn = self.get_by_role("button", name="Clear filters and sorters")
        self.text_promo_list = self.get_by_text("Promotion List")
        self.active_bbtn = self.get_by_role("button", name="Active")
        self.inactive_bttn = self.get_by_role("button", name="Inactive")
        self.edit_bttn =self.get_by_text("Edit")
        self.update_bttn = self.get_by_role("button", name="Yes, Update it!")
        self.ok_bbtn = self.get_by_role("button", name="OK", exact=True)

        self.liftime_promo = self.get_by_role("heading", name="Lifetime")
        self.period_promo = self.get_by_role("heading", name="Period")
        self.set_date_promo = self.get_by_role("heading", name="Set The Date")

        self.promo_code = self.get_by_placeholder("Promotion Code")
        self.promo_name_fill = self.get_by_placeholder("Promotion Name")
        self.promo_desc =self.get_by_placeholder("Promotion Description")
        self.start_date = self.page.locator("#startDate").get_by_placeholder("Select date")
        self.end_date = self.page.locator('xpath=//*[@id="endDate"]/div/input')
        self.next_year_bttn = self.get_by_title("Next year (Control + right)")
        self.next_month_bttn = self.get_by_title("Next month (PageDown)")
        self.show_merch = self.get_by_role("button", name="Show Merchant")
        self.submit_list_bttn = self.get_by_label("List Merchant").get_by_role("button", name="Submit")
        self.tier_choice = self.get_by_role("row", name="Tier Name Multiplier Merchant").get_by_label("")
        self.submit_bttn = self.get_by_role("button", name="Submit")
        self.cancel_bttn = self.get_by_role("button", name="Cancel")

        self.add_point_bttn = self.get_by_role("button", name="Add point rule for this")
        self.delete_bttn = self.get_by_role("button", name="Delete")
        self.cancel_bttn = self.get_by_role("button", name="Cancel")
        self.ok_bttn = self.get_by_role("button", name="OK")

        self.add_rule_opt_1 = self.page.locator("#ruleId div").nth(1)
        # self.ok_bbtn = self.get_by_role("button", name="OK")

    def promo_name(self, bttn_name):
        return self.page.get_by_role("button", name=bttn_name)

    def get_date(self, date):
        return self.get_by_title(date).locator("div")

    def get_rule_name(self,rule_name:str):
        return self.get_by_role("option", name=rule_name)

    def set_rule_name(self,rule_names):
        for index, rule in enumerate(rule_names):
            self.add_point_bttn.click()  # Click "Add point rule for this"
            print("🟢 Clicked 'Add point rule for this' Button")
            add_rule_button = self.page.locator("#ruleId div").nth(index + 1)  # Click dynamic nth element
            add_rule_button.click()  # Click to add rule box
            print(f"🟢 Clicked Add Rule Box {index + 1}")
            
            rule_option = self.get_rule_name(rule)  # Get the rule locator
            rule_option.click()  # Click the rule name
            print(f"✅ Added Rule: {rule}")  # Print confirmation

    def create_promotion(self, promo_code:str, promo_name:str, promo_desc:str,start_date:str, end_date:str, rule_name, item):
        test_case = item.name
        self.promo_bttn.click()
        self.liftime_promo.click()
        self.promo_code.fill(promo_code)
        self.promo_name_fill.fill(promo_name)
        self.promo_desc.fill(promo_desc)
        self.page.screenshot(path=f"screenshots/{test_case}_fill_promo.png")
        self.start_date.click()
        self.get_date(start_date).click()
        time.sleep(3)
        self.get_date(end_date).click()
        self.page.screenshot(path=f"screenshots/{test_case}_fill_date.png")
        self.show_merch.click()
        self.page.screenshot(path=f"screenshots/{test_case}_merchant_list.png")
        self.submit_list_bttn.click()
        time.sleep(3)
        self.tier_choice.click()
        self.set_rule_name(rule_name)
        self.page.screenshot(path=f"screenshots/{test_case}_fill_rule.png")
        self.submit_bttn.click()
        time.sleep(3)
        self.page.screenshot(path=f"screenshots/{test_case}_result.png")
        self.ok_bbtn.click()

    # def edit_promotion(self, ):

        

