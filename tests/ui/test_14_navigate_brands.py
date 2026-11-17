from pages.home_page import HomePage
from pages.products_page import ProductsPage
from playwright.sync_api import Page, expect


def test_14_navigate_product_brands(page: Page):
    home = HomePage(page)
    products = ProductsPage(page)

    home.open()
    home.go_to_products()
    products.select_brand("Polo")

    expect(page.get_by_text("Brand - Polo Products")).to_be_visible()
