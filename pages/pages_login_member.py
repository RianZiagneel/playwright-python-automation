import json
import hashlib
import hmac
import base64
from playwright.sync_api import APIRequestContext, Page
from pages.base_page import BasePage  

class LoginOneFlow(BasePage):
    SECRET_KEY = "3a7532509d5ecd5d9d07ba28a9da06e4dc27b105f36b90b6c05053919c8a59b6"
    APP_KEY = "3a7532509d5ecd5d9d07ba28a9da06e4dc27b105f36b90b6c05053919c8a59b6"
    APP_ID = "BLBR9793"
    MILLIS = "0042"

    def __init__(self, page: Page, request_context: APIRequestContext):
        super().__init__(page)
        self.request_context = request_context

    def get_token(self):
        """Fetch authentication token via API request."""
        headers = {
            "Content-Type": "application/json",
            "appKey": self.APP_KEY,
            "appId": self.APP_ID,
        }
        params = {"appKey": self.APP_KEY, "appId": self.APP_ID}

        response = self.request_get("/lifestyle-ws-goodie/api-rest/merchant/appToken", headers=headers, params=params)
        
        assert response.ok, f"Failed to get auth token: {response.text}"
        return response.json()["token"]
    
    def generate_signature(self, user_data: str):
        """Generate HMAC-SHA256 signature."""
        md5_body = hashlib.md5(user_data.encode()).hexdigest()
        string_to_sign = f"{md5_body}-{self.MILLIS}"
        hmac_str = hmac.new(self.SECRET_KEY.encode(), string_to_sign.encode(), hashlib.sha256).digest()
        return base64.b64encode(hmac_str).decode()

    def login_member(self, username: str, phone_number: str, full_name: str):
        """Perform API login and navigate to microsite."""
        bl_token = self.get_token()
        user_data = {"username": username, "phoneNumber": phone_number, "fullName": full_name}
        user_data_str = json.dumps(user_data, separators=(',', ':'))
        signature = self.generate_signature(user_data_str)
        headers = {
            "appToken": bl_token,
            "signature": signature,  # Replace with actual signature if needed
            "milliseconds": self.MILLIS,
            "Content-Type": "application/json",
        }

        response = self.request_post("/lifestyle-ws-goodie/api-rest/authentication/microsite/create", headers=headers, data=user_data)
        assert response.ok, f"Failed to create microsite session: {response.text}"
        # print(response)
        print(response.json()["urlMicrosite"])
        microsite_url = response.json()["urlMicrosite"]
        self.goto(microsite_url)
        self.page.screenshot(path="screenshots/login_member.png")

        return bl_token, microsite_url  # Return token so it can be used in another page
    
    def login_member_aja(self):
        """Perform API login and navigate to microsite."""
        bl_token = self.get_token()
        user_data = {"username":"jazz.kvlar@gmail.com", "phoneNumber":"62876620760345", "fullName":"Ajazz Kuvlar"}
        user_data_str = json.dumps(user_data, separators=(',', ':'))
        signature = self.generate_signature(user_data_str)
        headers = {
            "appToken": bl_token,
            "signature": signature,  # Replace with actual signature if needed
            "milliseconds": self.MILLIS,
            "Content-Type": "application/json",
        }

        response = self.request_post("/lifestyle-ws-goodie/api-rest/authentication/microsite/create", headers=headers, data=user_data)
        assert response.ok, f"Failed to create microsite session: {response.text}"
        # print(response)
        print(response.json()["urlMicrosite"])
        microsite_url = response.json()["urlMicrosite"]
        self.goto(microsite_url)
        # self.page.screenshot(path="screenshots/login_member_2.png")

        return bl_token, microsite_url  # Return token so it can be used in another page
        
    

        
