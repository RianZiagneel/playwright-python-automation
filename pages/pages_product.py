from pages.base_page import BasePage

import time

class ProductPage(BasePage):
    def __init__(self, page):
        super().__init__(page) 
        self.m_prod_page = self.page.get_by_role("link", name="Product") 
        self.voucher = self.get_by_role("heading", name="Voucher") 
        self.product_list = self.get_by_role("heading", name="Product List") 
        self.product_code = self.get_by_placeholder("Product Code") 
        self.product_name = self.get_by_placeholder("Product Name") 
        self.product_desc_html = self.page.locator("iframe[title=\"Rich Text Editor\\, editor1\"]").content_frame.locator("html") 
        self.product_desc_body = self.page.locator("iframe[title=\"Rich Text Editor\\, editor1\"]").content_frame.locator("body") 
        self.paragraph_fill = self.page.locator("iframe[title=\"Rich Text Editor\\, editor1\"]").content_frame.get_by_role("paragraph")
        self.product_show_merchant = self.get_by_role("button", name="Show Merchant") 
        self.product_submit_list = self.get_by_label("List Merchant").get_by_role("button", name="Submit") 
        self.product_image_upload = self.get_by_role("button", name="icon: plus Upload") 
        self.product_base_price = self.get_by_label("Base Price") 
        self.product_voucher_value = self.get_by_label("Voucher Value") 
        self.product_market_toggle = self.get_by_label("Marketplace Product") 
        self.product_submit_bttn = self.get_by_role("button", name="Submit") 
        self.product_back_bttn = self.get_by_role("button", name="Back")

        self.edit_bttn = self.get_by_role("button", name="Edit") 
        self.add_stock_bttn = self.get_by_role("button", name="Add Stock") 
        self.delete_bttn = self.get_by_role("button", name="Delete") 
        self.ok_bttn = self.get_by_role("button", name="OK")
        self.search_product = self.get_by_placeholder("Search products by name")
        self.select_date = self.get_by_placeholder("Select date")
        self.generate_voucher = self.get_by_role("button", name="Generate Voucher")
        self.add_stock = self.get_by_role("spinbutton", name="* Additional Stock:")
        self.gen_bttn = self.get_by_role("button", name="Generate")
        self.save_bttn = self.get_by_role("button", name="Save")
        self.yes_bttn = self.get_by_role("button", name="Yes, delete it!")
        

    def get_date(self, date):
        return self.get_by_title(date).locator("div")
    
        