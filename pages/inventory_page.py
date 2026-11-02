from playwright.sync_api import Page, expect


class InventoryPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.inventory = page.locator("[data-test='inventory-container']")
        self.cart_link = page.locator("[data-test='shopping-cart-link']")
        self.cart_badge = page.locator("[data-test='shopping-cart-badge']")

    def expect_loaded(self) -> None:
        expect(self.inventory).to_be_visible()

    def add_item_to_cart(self, item_name: str) -> None:
        item = self.page.locator(".inventory_item").filter(has_text=item_name)
        item.get_by_role("button", name="Add to cart").click()

    def expect_cart_count(self, count: int) -> None:
        expect(self.cart_badge).to_have_text(str(count))

    def open_cart(self) -> None:
        self.cart_link.click()
