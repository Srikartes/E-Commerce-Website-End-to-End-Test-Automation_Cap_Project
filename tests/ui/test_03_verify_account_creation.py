from pages.auth_page import AuthPage
from pages.home_page import HomePage
from playwright.sync_api import Page, expect


def test_03_verify_successful_account_creation(page: Page, user_data):
    home = HomePage(page)
    auth = AuthPage(page)

    home.open()
    home.go_to_login()
    auth.signup_initial(user_data["name"], user_data["email"])
    auth.fill_account_details(user_data)

    expect(page.locator("h2[data-qa='account-created']")).to_have_text(
        "Account Created!"
    )
    auth.click_continue()
    expect(page.get_by_text(f"Logged in as {user_data['name']}")).to_be_visible()
    auth.delete_account()
