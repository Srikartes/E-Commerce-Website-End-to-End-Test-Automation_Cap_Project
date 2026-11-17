import re
from pages.home_page import HomePage
from playwright.sync_api import Page, expect


def test_07_navigate_to_products_page(page: Page):
    home = HomePage(page)

    home.open()
    home.go_to_products()

    expect(page).to_have_url(re.compile(r".*/products"))
    expect(page.get_by_role("heading", name="All Products")).to_be_visible()
