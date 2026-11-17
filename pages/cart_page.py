from pages.base_page import BasePage


class CartPage(BasePage):

    def remove_product(self, product_id=1):
        self.page.locator(f"#product-{product_id} a.cart_quantity_delete").click()
