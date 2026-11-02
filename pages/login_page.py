from playwright.sync_api import Page, expect


class LoginPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.username = page.get_by_placeholder("Username")
        self.password = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.error = page.locator("[data-test='error']")

    def open(self, base_url: str) -> None:
        self.page.goto(base_url)

    def login(self, username: str, password: str) -> None:
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()

    def expect_error(self, message: str) -> None:
        expect(self.error).to_contain_text(message)
