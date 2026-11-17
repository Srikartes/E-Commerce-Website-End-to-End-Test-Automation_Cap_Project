from pages.auth_page import AuthPage
from pages.home_page import HomePage
from playwright.sync_api import Page, expect


def test_04_login_with_valid_credentials(page: Page, registered_user):
    home = HomePage(page)
    auth = AuthPage(page)

    home.open()
    home.go_to_login()
    auth.login(registered_user["email"], registered_user["password"])

    expect(
        page.get_by_text(f"Logged in as {registered_user['name']}")
    ).to_be_visible()
