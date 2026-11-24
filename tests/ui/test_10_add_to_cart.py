import pytest
from playwright.sync_api import Page, expect
from pages.home_page import HomePage


@pytest.mark.ui
def test_10_add_product_to_cart(page: Page):
    home = HomePage(page)

    home.open()
    home.go_to_products()

    add_btn = page.locator(".productinfo a[data-product-id='1']").first
    add_btn.scroll_into_view_if_needed()
    add_btn.click()

    expect(page.locator("#cartModal")).to_be_visible(timeout=10000)
    page.locator("#cartModal a[href='/view_cart']").click()

    expect(page.locator("#product-1")).to_be_visible()
