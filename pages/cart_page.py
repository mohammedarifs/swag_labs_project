from playwright.sync_api import Page, expect


class CartPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.cart_items = page.locator(".cart_item")

    def expect_item(self, item_name: str) -> None:
        expect(self.cart_items.filter(has_text=item_name)).to_be_visible()
