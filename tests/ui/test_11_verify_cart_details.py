import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


@pytest.mark.ui
def test_11_verify_product_details_and_quantity_in_cart(page: Page):
    home = HomePage(page)
    products = ProductsPage(page)
    cart = CartPage(page)

    home.open()
    home.go_to_products()
    products.view_product_details(1)
    products.set_quantity_and_add(4)

    cart.verify_product_in_cart(
        product_id=1,
        expected_name="Blue Top",
        expected_price="Rs. 500",
        expected_qty="4",
    )
