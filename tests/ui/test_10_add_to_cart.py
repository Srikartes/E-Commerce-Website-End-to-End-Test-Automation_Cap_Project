from pages.home_page import HomePage
from playwright.sync_api import Page, expect


def test_10_add_product_to_cart(page: Page):
    home = HomePage(page)

    home.open()
    home.go_to_products()

    # Click the visible 'Add to cart' button on the first product card
    page.locator("a[data-product-id='1']").first.click()

    # Wait for the confirmation modal and click 'View Cart'
    expect(page.locator("#cartModal")).to_be_visible()
    page.locator("#cartModal a[href='/view_cart']").click()

    # Verify the product is added in the cart table
    expect(page.locator("#product-1")).to_be_visible()
