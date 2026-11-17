from pages.auth_page import AuthPage
from pages.home_page import HomePage
from playwright.sync_api import Page, expect


def test_05_login_with_invalid_credentials(page: Page):
    home = HomePage(page)
    auth = AuthPage(page)

    home.open()
    home.go_to_login()
    auth.login("nonexistent_user_999@test.com", "InvalidPass123")

    expect(page.get_by_text("Your email or password is incorrect!")).to_be_visible()
