from playwright.sync_api import sync_playwright

def test_get():
    with sync_playwright() as playwright:
        # browser = playwright.chromium.launch()
        api_request_context = playwright.request.new_context(base_url = "https://staging-loyalty.bersama.id/lifestyle-ws-goodie/api-rest/merchant/appToken")
        
        headers = {
            "AppKey": "313dd216413c1a7ca87c0642f37cffb4b6d019dd6e811adaa136e0419530aaf9",
            "AppId": "BLBR6424"
        }
        
        response = api_request_context.get(url="https://staging-loyalty.bersama.id/lifestyle-ws-goodie/api-rest/merchant/appToken", headers=headers)
        
        print(response.status_code)

        assert response.ok
 
        

        

       
