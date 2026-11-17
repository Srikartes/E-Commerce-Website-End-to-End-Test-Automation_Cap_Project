from pages.home_page import HomePage
from playwright.sync_api import Page, expect


def test_08_search_product_and_verify(page: Page):
    home = HomePage(page)

    home.open("/products")

    # Type into search box and click search button
    search_input = page.locator("#search_product")
    expect(search_input).to_be_visible()
    search_input.fill("Blue Top")

    # Click search button and wait for the 'Searched Products' heading
    page.locator("#submit_search").click()

    expect(page.locator("h2.title.text-center")).to_have_text(
        "Searched Products"
    )
    expect(
        page.locator(".features_items .productinfo p").first
    ).to_have_text("Blue Top")
