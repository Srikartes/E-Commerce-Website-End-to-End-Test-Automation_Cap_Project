from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.cart_table = page.locator("#cart_info_table")
        self.empty_cart_message = page.locator("#empty_cart")

    def verify_product_in_cart(self, product_id: int, expected_name: str, expected_price: str, expected_qty: str):
        row = self.page.locator(f"#product-{product_id}")
        expect(row).to_be_visible(timeout=15000)
        expect(row.locator(".cart_description h4 a")).to_have_text(expected_name)
        expect(row.locator(".cart_price p")).to_have_text(expected_price)
        expect(row.locator(".cart_quantity button")).to_have_text(expected_qty)

    def remove_product(self, product_id: int):
        self.page.wait_for_load_state("load")
        delete_btn = self.page.locator(f"#product-{product_id} a.cart_quantity_delete")
        delete_btn.scroll_into_view_if_needed()
        delete_btn.click()
        expect(self.page.locator(f"#product-{product_id}")).to_have_count(0, timeout=15000)
