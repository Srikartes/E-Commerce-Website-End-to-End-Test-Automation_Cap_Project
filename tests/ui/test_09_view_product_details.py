from pages.home_page import HomePage
from pages.products_page import ProductsPage
from playwright.sync_api import Page, expect


def test_09_view_product_details(page: Page):
    home = HomePage(page)
    products = ProductsPage(page)

    home.open()
    home.go_to_products()
    products.view_product_details(product_id=1)

    expect(page.locator(".product-information")).to_be_visible()
    expect(page.get_by_role("heading", name="Blue Top")).to_be_visible()
