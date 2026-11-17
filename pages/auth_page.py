from pages.base_page import BasePage


class AuthPage(BasePage):

    def signup_initial(self, name: str, email: str):
        self.page.locator("input[data-qa='signup-name']").fill(name)
        self.page.locator("input[data-qa='signup-email']").fill(email)
        self.page.locator("button[data-qa='signup-button']").click()

    def fill_account_details(self, user: dict):
        self.page.locator("#id_gender1").check()
        self.page.locator("#password").fill(user["password"])
        self.page.locator("#days").select_option(user["birth_date"])
        self.page.locator("#months").select_option(user["birth_month"])
        self.page.locator("#years").select_option(user["birth_year"])
        self.page.locator("#newsletter").check()
        self.page.locator("#optin").check()

        self.page.locator("#first_name").fill(user["firstname"])
        self.page.locator("#last_name").fill(user["lastname"])
        self.page.locator("#company").fill(user["company"])
        self.page.locator("#address1").fill(user["address1"])
        self.page.locator("#address2").fill(user["address2"])
        self.page.locator("#country").select_option(user["country"])
        self.page.locator("#state").fill(user["state"])
        self.page.locator("#city").fill(user["city"])
        self.page.locator("#zipcode").fill(user["zipcode"])
        self.page.locator("#mobile_number").fill(user["mobile_number"])
        self.page.locator("button[data-qa='create-account']").click()

    def click_continue(self):
        self.page.locator("a[data-qa='continue-button']").click()

    def login(self, email: str, password: str):
        self.page.locator("input[data-qa='login-email']").fill(email)
        self.page.locator("input[data-qa='login-password']").fill(password)
        self.page.locator("button[data-qa='login-button']").click()

    def logout(self):
        self.page.get_by_role("link", name="Logout").click()

    def delete_account(self):
        self.page.get_by_role("link", name="Delete Account").click()
