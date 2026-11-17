from pages.home_page import HomePage
from playwright.sync_api import Page, expect

import pytest
@pytest.mark.ui
@pytest.mark.smoke
def test_01_home_page_loads(page: Page):
    home = HomePage(page)
    home.open()
    expect(page).to_have_title("Automation Exercise")
    #assert false