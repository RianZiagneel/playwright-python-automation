from pages.base_page import BasePage

import time
class ReportPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        #page Report
        self.point_report = self.get_by_role("img", name="Loyalty Points Activity")
        self.search_by_name = self.get_by_role("textbox", name="Search By Member Name")
        self.start_date = self.get_by_role("textbox", name="Select start date")
        self.end_date = self.get_by_role("textbox", name="Select end date")
        self.trx_type = self.page.get_by_title("Select Transaction Type")
        self.issuing_opt = self.get_by_role("option", name="Issuing")
        self.reedem_opt = self.get_by_role("option", name="Redeem")
        self.clear_filter = self.get_by_role("button", name="Clear Filters")
        self.dowload_report = self.get_by_role("button", name="icon: download Download")
        self.table_locator = self.page.locator("tr.ant-table-row")
                                             