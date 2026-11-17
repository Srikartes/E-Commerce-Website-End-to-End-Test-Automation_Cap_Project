from pages.auth_page import AuthPage
from pages.home_page import HomePage
from playwright.sync_api import Page, expect
import pytest
@pytest.mark.ui
@pytest.mark.regression


def test_02_register_new_user(page: Page, user_data):
    home = HomePage(page)
    auth = AuthPage(page)

    home.open()
    home.go_to_login()
    auth.signup_initial(user_data["name"], user_data["email"])
    auth.fill_account_details(user_data)

    expect(page.locator("h2[data-qa='account-created']")).to_be_visible()
    auth.click_continue()
    auth.delete_account()
