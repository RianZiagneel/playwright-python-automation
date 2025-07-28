import json
import hashlib
import hmac
import base64
import uuid
from playwright.sync_api import APIRequestContext, Page
from pages.base_page import BasePage 
from pages.pages_login_member import LoginOneFlow
from pages.pages_login_merchant import LoginPage
from pages.page_dash_merchant import DashPage


class PointIssue(BasePage):
    SECRET_KEY = "3a7532509d5ecd5d9d07ba28a9da06e4dc27b105f36b90b6c05053919c8a59b6"
    MILLIS = "0042"


    def __init__(self, page, request_context, auth_token):
        super().__init__(page)
        self.request_context = request_context
        self.auth_token = auth_token  # Token from LoginPage

    def generate_signature(self, payload_str: str):
        """Generate HMAC-SHA256 signature."""
        md5_body = hashlib.md5(payload_str.encode()).hexdigest()
        string_to_sign = f"{md5_body}-{self.MILLIS}"
        hmac_str = hmac.new(self.SECRET_KEY.encode(), string_to_sign.encode(), hashlib.sha256).digest()
        return base64.b64encode(hmac_str).decode()

    def issue_point(self, rule_code: str, member_id: str, merchant_id: str, ref_id: str, trx_amount: float):
        """Handles issuing points request."""
        user_data = {
            "ruleCode": rule_code,
            "memberId": member_id,
            "merchantId": merchant_id,
            "refId": ref_id,
            "totalTrxAmount": trx_amount
        }

        payload_str = json.dumps(user_data, separators=(',', ':'))
        signature = self.generate_signature(payload_str)

        headers = {
            "appToken": self.auth_token,  # Using token from LoginPage
            "signature": signature,
            "milliseconds": self.MILLIS,
            "Content-Type": "application/json",
        }

        response = self.request_post("/lifestyle-ws-goodie/api-rest/promotion/posting/microsite", headers=headers, data=user_data)
        print(response.json())
        assert response.ok, f"Failed to issue points: {response.text}"
        return response.json()
    
    def issue_point_aja(self):
        """Handles issuing points request."""

        ref_id = str(uuid.uuid4())
        user_data = {
            "ruleCode": "Test_QA_AJ_2",
            "memberId": "BD0894D0-55B4-4313-B8E0-65E3BE2D8B35",
            "merchantId": "DDC5520D-2340-4EC2-AAB6-279EF59984EE",
            "refId": ref_id,
            "totalTrxAmount": 100000
        }

        payload_str = json.dumps(user_data, separators=(',', ':'))
        signature = self.generate_signature(payload_str)

        headers = {
            "appToken": self.auth_token,  # Using token from LoginPage
            "signature": signature,
            "milliseconds": self.MILLIS,
            "Content-Type": "application/json",
        }

        response = self.request_post("/lifestyle-ws-goodie/api-rest/promotion/posting/microsite", headers=headers, data=user_data)
        print(response.json())
        assert response.ok, f"Failed to issue points: {response.text}"
        return response.json()
    
 