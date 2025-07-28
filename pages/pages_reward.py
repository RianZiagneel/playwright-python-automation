from pages.base_page import BasePage

import time

class RewardPage(BasePage):
    def __init__(self, page):
        super().__init__(page)    
        self.m_reward_bttn = self.get_by_role("link", name="Reward")
        self.own_product = self.get_by_role("heading", name="Own Product")
        self.reward_list = self.get_by_role("heading", name="Reward List")
        self.colaboration = self.get_by_role("heading", name="Collaboration")
        page.get_by_placeholder("Reward Code").click()
        page.get_by_placeholder("Reward Name").click()
        page.get_by_placeholder("Select date").click()
        page.get_by_title("Next year (Control + right)").click()
        page.get_by_title("March 7, 2026").locator("div").click()
        page.get_by_role("row", name="Tier Name").get_by_label("").check()
        page.locator("#redeemFrequency svg").click()
        page.get_by_role("option", name="Multiple").click()
        page.locator("#productId svg").click()
        page.get_by_role("option", name="Test 123 Automation").click()
        page.get_by_label("Increase Value").click()
        page.get_by_label("Point Required").click()
        page.get_by_label("Point Required").fill("1")
        page.locator("iframe[title=\"Rich Text Editor\\, editor3\"]").content_frame.get_by_role("paragraph").click()
        page.locator("iframe[title=\"Rich Text Editor\\, editor3\"]").content_frame.locator("body").fill("test")
        page.locator("iframe[title=\"Rich Text Editor\\, editor4\"]").content_frame.get_by_role("paragraph").click()
        page.locator("iframe[title=\"Rich Text Editor\\, editor4\"]").content_frame.locator("body").fill("test")
        page.get_by_role("button", name="Submit").click()
        page.get_by_role("button", name="Submit").click()
        page.get_by_role("button", name="Back").click()