from playwright.sync_api import Page, Locator

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self, url:str):
        self.page.goto(url)

    def get_text (self, locator:Locator) -> str:
        return locator.text_content()
    
    def click(self, locator: Locator):
        locator.click()

    def fill(self, locator:Locator, text:str):
        locator.fill(text)
    
    def get_by_placeholder(self, placeholder:str) -> Locator:
        return self.page.get_by_placeholder(placeholder)

    def get_by_label(self, label:str) -> Locator:
        return self.page.get_by_label(label)
    
    def get_by_role(self, role:str, **kwargs) -> Locator:
        return self.page.get_by_role(role, **kwargs)
    
    def get_by_text(self, text:str) -> Locator:
        return self.page.get_by_text(text)
    
    def get_by_title(self,text:str)-> Locator:
        return self.page.get_by_title(text)
    
    
# --------- API REQUEST METHODS ---------
    def request_get(self, url: str, headers: dict = None, params: dict = None):
        response = self.request_context.get(url, headers=headers, params=params)
        return response

    def request_post(self, url: str, headers: dict = None, data: dict = None):
        response = self.request_context.post(url, headers=headers, data=data)
        return response

    def request_put(self, url: str, headers: dict = None, data: dict = None):
        response = self.request_context.put(url, headers=headers, data=data)
        return response

    def request_delete(self, url: str, headers: dict = None):
        response = self.request_context.delete(url, headers=headers)
        return response

