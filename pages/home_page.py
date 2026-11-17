from pages.base_page import BasePage


class HomePage(BasePage):

    def go_to_login(self):
        self.page.get_by_role("link", name="Signup / Login").click()

    def go_to_products(self):
        self.page.get_by_role("link", name="Products").click()

    def go_to_cart(self):
        self.page.get_by_role("link", name="Cart").click()

    def subscribe_in_footer(self, email: str):
        self.page.locator("#footer").scroll_into_view_if_needed()
        self.page.locator("#susbscribe_email").fill(email)
        self.page.locator("#subscribe").click()
