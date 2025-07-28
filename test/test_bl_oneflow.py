import requests
import pytest
import json
from collections import OrderedDict
import urllib.parse
import hashlib
import hmac
import base64
import os
import pytest_html
import pytest_html_reporter
from playwright.sync_api import Playwright, sync_playwright


@pytest.mark.order(1)    
def test_bl_one_flow(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(proxy={"server": "10.90.2.105:3128",})
        context = browser.new_context(base_url = "https://staging-loyalty.bersama.id")
        api_request_context = context.request
        page = context.new_page()

        extra_http_headers={
                "Content-Type": "application/json",
                "appKey": "313dd216413c1a7ca87c0642f37cffb4b6d019dd6e811adaa136e0419530aaf9",
                "appId": "BLBR6424"
                    }
        param={
                "appKey": "313dd216413c1a7ca87c0642f37cffb4b6d019dd6e811adaa136e0419530aaf9",
                "appId": "BLBR6424"
                }
                

        payload ={}
        response = api_request_context.get("/lifestyle-ws-goodie/api-rest/merchant/appToken",params=param,headers=extra_http_headers,ignore_https_errors=True)
        assert response.ok
        assert response.json 
        obj = response.json()
        # json_formatted_str = json.dumps(obj, indent=4) just for reference
        print("response",response)
        print(response.url)
        print("ouput",response.json())
        print("tokn",obj["token"])
        assert response.status == 200
               
        bl_token = obj["token"]

        payload={
            "username":"jazz.kvlar@gmail.com",
            "phoneNumber":"62876620760345",
            "fullName":"Ajazz Kuvlar"
        }
        
        payload_str = json.dumps(payload, separators=(',', ':'))
        comp_payload = payload_str.replace(", ", ",")
        md5_body = hashlib.md5(comp_payload.encode()).hexdigest()
        string_to_sign = f"{md5_body}-0042"
        scrt_key = "313dd216413c1a7ca87c0642f37cffb4b6d019dd6e811adaa136e0419530aaf9"
        hmac_str = hmac.new(scrt_key.encode(), string_to_sign.encode(), hashlib.sha256).digest()
        signature = base64.b64encode(hmac_str).decode()

        headers = {
            'appToken': bl_token,
            'signature': signature,
            'milliseconds': '0042',
            'Content-Type': 'application/json'
            }

        resp_microsite = api_request_context.post("lifestyle-ws-goodie/api-rest/authentication/microsite/create",headers=headers,data=payload,)
        print("json microsite",resp_microsite.json())
        json_resp = resp_microsite.json()
        url_micro = json_resp["urlMicrosite"]
        print("url",url_micro)
        page.goto(url_micro)
        page.screenshot(path="screenshot_home.png")
        return url_micro

        


        
        
  

