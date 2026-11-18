# from pages.base_page import BasePage


# class ProductsPage(BasePage):

#     def search_product(self, product_name: str):
#         self.page.locator("#search_product").fill(product_name)
#         self.page.locator("#submit_search").click()

#     def view_product_details(self, product_id=1):
#         self.page.locator(f"a[href='/product_details/{product_id}']").click()

#     def add_product_to_cart(self):
#         self.page.get_by_role("button", name="Add to cart").click()
#         self.page.get_by_role("link", name="View Cart").click()

#     def select_category(self, main_category: str, sub_category: str):
#         self.page.locator(f"a[href='#{main_category}']").click()
#         self.page.get_by_role("link", name=sub_category).click()

#     def select_brand(self, brand_name: str):
#         self.page.locator(f"a[href='/brand_products/{brand_name}']").click()

from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class ProductsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.search_input = page.locator("#search_product")
        self.search_button = page.locator("#submit_search")
        self.searched_products_heading = page.get_by_role("heading", name="Searched Products")
        self.product_cards = page.locator(".features_items .product-image-wrapper")
        self.quantity_input = page.locator("#quantity")
        self.add_to_cart_detail_btn = page.locator("button.cart")
        self.continue_shopping_btn = page.get_by_role("button", name="Continue Shopping")
        self.view_cart_link = page.locator("#cartModal a[href='/view_cart']")
        self.cart_modal = page.locator("#cartModal")

    def open(self, path: str = "/products"):
        super().open(path)

    def search_product(self, product_name: str):
        self.search_input.fill(product_name)
        self.search_button.click()

    def view_product_details(self, product_id: int = 1):
        link = self.page.locator(f"a[href='/product_details/{product_id}']").first
        link.scroll_into_view_if_needed()
        link.click()
        if "google_vignette" in self.page.url or f"/product_details/{product_id}" not in self.page.url:
            self.page.goto(f"https://automationexercise.com{product_id}", wait_until="load")

    def view_first_product_details(self):
        self.view_product_details(1)

    def add_product_by_id(self, product_id: int = 1, view_cart: bool = False):
        self.page.wait_for_load_state("load")
        add_btn = self.page.locator(f".productinfo a[data-product-id='{product_id}']").first
        add_btn.scroll_into_view_if_needed()
        add_btn.click()

        expect(self.cart_modal).to_be_visible(timeout=15000)
        if view_cart:
            self.view_cart_link.click()
        else:
            self.continue_shopping_btn.click()
            expect(self.cart_modal).to_be_hidden()

    def add_product_to_cart(self, product_id: int = 1, quantity: int | None = None, view_cart: bool = False):
        if self.add_to_cart_detail_btn.is_visible():
            if quantity is not None:
                self.quantity_input.fill(str(quantity))
            self.add_to_cart_detail_btn.click()
            expect(self.cart_modal).to_be_visible(timeout=15000)
            if view_cart:
                self.view_cart_link.click()
            else:
                self.continue_shopping_btn.click()
                expect(self.cart_modal).to_be_hidden()
            return

        self.add_product_by_id(product_id=product_id, view_cart=view_cart)

    def set_quantity_and_add(self, quantity: int):
        self.page.wait_for_load_state("load")
        self.quantity_input.fill(str(quantity))
        self.add_to_cart_detail_btn.click()
        expect(self.cart_modal).to_be_visible(timeout=15000)
        self.view_cart_link.click()

    def select_category(self, main_category: str, sub_category: str):
        category_id = main_category.strip().capitalize()
        main_link = self.page.locator(f".category-products a[href='#{category_id}']")
        main_link.scroll_into_view_if_needed()
        main_link.click()

        sub_menu = self.page.locator(f"#{category_id}")
        expect(sub_menu).to_be_visible(timeout=10000)

        sub_link = sub_menu.locator(f".panel-body a:has-text('{sub_category}')").first
        sub_link.click()

    def select_brand(self, brand_name: str):
        brand_link = self.page.locator(f".brands-name a:has-text('{brand_name}')")
        brand_link.scroll_into_view_if_needed()
        brand_link.click()
