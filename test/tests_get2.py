import requests
import pytest
import json


from playwright.sync_api import Playwright, sync_playwright

def test_get():
    def run(playwright: Playwright) -> None:

        param={
                "AppKey": "313dd216413c1a7ca87c0642f37cffb4b6d019dd6e811adaa136e0419530aaf9",
                "AppId": "BLBR6424"
        }
        extra_http_headers={
                "Content-Type": "application/json",
                "AppKey": "313dd216413c1a7ca87c0642f37cffb4b6d019dd6e811adaa136e0419530aaf9",
                "AppId": "BLBR6424"
            }
        base_url = "https://staging-loyalty.bersama.id/lifestyle-ws-goodie/api-rest/merchant/appToken"
        payload ={}
        
        resp = requests.get(url=base_url,params=param,headers=extra_http_headers,data=payload)
        obj = json.loads(resp.text)
        json_formatted_str = json.dumps(obj, indent=4)
        print(obj['token'])
        print(json_formatted_str)
        print(resp)
        print(resp.text)
        print(resp.json())
        print(resp.status_code)
        # print(resp.json())

    with sync_playwright() as playwright:
        run(playwright)

def test_post():
    def run(playwright: Playwright) -> None:
        url = "https://staging-loyalty.bersama.id/lifestyle-ws-goodie/api-rest/promotion/posting/micrositeauthentication/microsite/create"

        payload={
            "fullName":"Coba register tiga",
            "username":"coba.register003@mailinator.com",
            "phoneNumber":"6289876548765"

        }
        headers = {
            'appToken': '34312B28-FF38-4061-A3D5-59864CC284A9',
            'signature': '79N2MgToaoWB7V4C8/FkcmjF6r0IGzQy+fFVbdCvbmo=',
            'milliseconds': '0042',
            'Content-Type': 'application/json'
            }

        resp = requests.post(url=url,headers=headers,data=payload)
        obj = json.loads(resp.text)
        json_formatted_str = json.dumps(obj, indent=4)
        # print(obj['token'])
        print(json_formatted_str)
        print(resp)
        print(resp.text)
        print(resp.json())
        print(resp.status_code)
        
    with sync_playwright() as playwright:
        run(playwright)