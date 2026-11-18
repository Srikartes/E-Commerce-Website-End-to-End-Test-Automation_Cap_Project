# from pages.cart_page import CartPage
# from pages.home_page import HomePage
# from pages.products_page import ProductsPage
# from playwright.sync_api import Page, expect

# import pytest
# @pytest.mark.ui

# def test_12_remove_product_from_cart(page: Page):
#     home = HomePage(page)
#     products = ProductsPage(page)
#     cart = CartPage(page)

#     home.open()
#     home.go_to_products()
#     products.view_product_details(product_id=1)
#     products.add_product_to_cart()

#     cart.remove_product(product_id=1)
#     expect(page.get_by_text("Cart is empty!")).to_be_visible()

import pytest
from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


@pytest.mark.ui
def test_12_remove_product_from_cart(page: Page):
    home = HomePage(page)
    products = ProductsPage(page)
    cart = CartPage(page)

    home.open()
    home.go_to_products()
    products.add_product_by_id(product_id=1, view_cart=True)

    expect(page.locator("#product-1")).to_be_visible()
    cart.remove_product(product_id=1)
    expect(cart.empty_cart_message).to_be_visible()
