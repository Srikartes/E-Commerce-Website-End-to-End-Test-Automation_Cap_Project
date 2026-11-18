# from pages.home_page import HomePage
# from pages.products_page import ProductsPage
# from playwright.sync_api import Page, expect

# import pytest
# @pytest.mark.ui

# def test_13_navigate_product_categories(page: Page):
#     home = HomePage(page)
#     products = ProductsPage(page)

#     home.open()
#     home.go_to_products()
#     products.select_category("Women", "Dress")

#     expect(page.get_by_text("Women - Dress Products")).to_be_visible()



import pytest
from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.products_page import ProductsPage


@pytest.mark.ui
def test_13_navigate_product_categories(page: Page):
    home = HomePage(page)
    products = ProductsPage(page)

    home.open()
    home.go_to_products()
    products.select_category("Women", "Dress")

    expect(page.get_by_text("Women - Dress Products")).to_be_visible()
