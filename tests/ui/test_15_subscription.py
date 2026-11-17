from pages.home_page import HomePage
from playwright.sync_api import Page, expect

import pytest
@pytest.mark.ui

def test_15_verify_subscription_functionality(page: Page, user_data):
    home = HomePage(page)
    home.open()
    home.subscribe_in_footer(user_data["email"])

    expect(page.get_by_text("You have been successfully subscribed!")).to_be_visible()
