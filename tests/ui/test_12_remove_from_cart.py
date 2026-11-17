from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from playwright.sync_api import Page, expect


def test_12_remove_product_from_cart(page: Page):
    home = HomePage(page)
    products = ProductsPage(page)
    cart = CartPage(page)

    home.open()
    home.go_to_products()
    products.view_product_details(product_id=1)
    products.add_product_to_cart()

    cart.remove_product(product_id=1)
    expect(page.get_by_text("Cart is empty!")).to_be_visible()
