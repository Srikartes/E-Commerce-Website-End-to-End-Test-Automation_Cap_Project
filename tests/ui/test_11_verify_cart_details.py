from pages.home_page import HomePage
from pages.products_page import ProductsPage
from playwright.sync_api import Page, expect


def test_11_verify_product_details_and_quantity_in_cart(page: Page):
    home = HomePage(page)
    products = ProductsPage(page)

    home.open()
    home.go_to_products()
    products.view_product_details(product_id=1)
    products.add_product_to_cart()

    expect(page.locator("#product-1 .cart_description h4")).to_have_text("Blue Top")
    expect(page.locator("#product-1 .cart_price p")).to_have_text("Rs. 500")
    expect(page.locator("#product-1 .cart_quantity button")).to_have_text("1")
