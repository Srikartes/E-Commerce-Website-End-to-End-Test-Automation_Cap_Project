# from pages.base_page import BasePage


# class HomePage(BasePage):

#     def go_to_login(self):
#         self.page.get_by_role("link", name="Signup / Login").click()

#     def go_to_products(self):
#         self.page.get_by_role("link", name="Products").click()

#     def go_to_cart(self):
#         self.page.get_by_role("link", name="Cart").click()

#     def subscribe_in_footer(self, email: str):
#         self.page.locator("#footer").scroll_into_view_if_needed()
#         self.page.locator("#susbscribe_email").fill(email)
#         self.page.locator("#subscribe").click()
from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.signup_login_link = page.get_by_role("link", name="Signup / Login")
        self.products_link = page.get_by_role("link", name="Products")
        self.cart_link = page.get_by_role("link", name="Cart")

    def open(self, path: str = "/"):
        super().open(path)

    def go_to_login(self):
        self.signup_login_link.click()
        if "google_vignette" in self.page.url or "/login" not in self.page.url:
            self.page.goto("https://automationexercise.com", wait_until="load")

    def go_to_products(self):
        self.products_link.click()
        if "google_vignette" in self.page.url or "/products" not in self.page.url:
            self.page.goto("https://automationexercise.com", wait_until="load")

    def go_to_cart(self):
        self.cart_link.click()
        if "google_vignette" in self.page.url or "/view_cart" not in self.page.url:
            self.page.goto("https://automationexercise.com", wait_until="load")

    def select_category(self, main_category: str, sub_category: str):
        category_id = main_category.strip().capitalize()
        main_link = self.page.locator(f".category-products a[href='#{category_id}']")
        main_link.scroll_into_view_if_needed()
        main_link.click()

        sub_menu = self.page.locator(f"#{category_id}")
        expect(sub_menu).to_be_visible(timeout=10000)

        sub_link = sub_menu.locator(f".panel-body a:has-text('{sub_category}')").first
        sub_link.click()
