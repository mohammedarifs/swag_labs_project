from playwright.sync_api import Page, expect


class CheckoutPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.first_name = page.get_by_test_id("firstName")
        self.last_name = page.get_by_test_id("lastName")
        self.postal_code = page.get_by_test_id("postalCode")
        self.error = page.locator("[data-test='error']")
        self.summary_items = page.locator(".cart_item")
        self.total = page.locator("[data-test='total-label']")
        self.complete_header = page.locator("[data-test='complete-header']")

    def start(self) -> None:
        self.page.get_by_test_id("checkout").click()

    def enter_details(self, first_name: str, last_name: str, postal_code: str) -> None:
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.postal_code.fill(postal_code)

    def continue_to_summary(self) -> None:
        self.page.get_by_test_id("continue").click()

    def expect_error(self, message: str) -> None:
        expect(self.error).to_contain_text(message)

    def expect_summary_item(self, item_name: str) -> None:
        expect(self.summary_items.filter(has_text=item_name)).to_be_visible()

    def expect_total_displayed(self) -> None:
        expect(self.total).to_be_visible()

    def finish_order(self) -> None:
        self.page.get_by_test_id("finish").click()

    def expect_order_confirmation(self) -> None:
        expect(self.complete_header).to_have_text("Thank you for your order!")
