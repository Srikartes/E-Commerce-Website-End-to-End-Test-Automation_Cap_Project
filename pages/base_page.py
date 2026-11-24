from playwright.sync_api import Page, expect


class BasePage:
    BASE_URL = "https://automationexercise.com"

    def __init__(self, page: Page):
        self.page = page
        self.subscription_input = page.locator("#susbscribe_email")
        self.subscription_button = page.locator("#subscribe")
        self.subscription_success = page.locator("#success-subscribe")

    def open(self, path: str = "/"):
        url = path if path.startswith("http") else f"{self.BASE_URL}{path}"
        self.page.goto(url, wait_until="load")

    def subscribe_in_footer(self, email: str):
        self.subscription_input.scroll_into_view_if_needed()
        self.subscription_input.fill(email)
        self.subscription_button.click()
        expect(self.subscription_success).to_be_visible(timeout=10000)
