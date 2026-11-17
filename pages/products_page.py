from pages.base_page import BasePage


class ProductsPage(BasePage):

    def search_product(self, product_name: str):
        self.page.locator("#search_product").fill(product_name)
        self.page.locator("#submit_search").click()

    def view_product_details(self, product_id=1):
        self.page.locator(f"a[href='/product_details/{product_id}']").click()

    def add_product_to_cart(self):
        self.page.get_by_role("button", name="Add to cart").click()
        self.page.get_by_role("link", name="View Cart").click()

    def select_category(self, main_category: str, sub_category: str):
        self.page.locator(f"a[href='#{main_category}']").click()
        self.page.get_by_role("link", name=sub_category).click()

    def select_brand(self, brand_name: str):
        self.page.locator(f"a[href='/brand_products/{brand_name}']").click()
