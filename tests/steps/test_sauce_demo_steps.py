from pytest_bdd import given, parsers, scenarios, then, when

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

scenarios("login.feature", "checkout.feature", "place_order.feature", "negative_scenarios.feature")


@given("the Sauce Demo login page is open")
def open_login_page(login_page: LoginPage, app_url: str) -> None:
    login_page.open(app_url)


@given(parsers.parse('I am logged in as "{username}"'))
def logged_in_as(login_page: LoginPage, app_url: str, username: str) -> None:
    login_page.open(app_url)
    login_page.login(username, "secret_sauce")


@when(parsers.parse('I log in with username "{username}" and password "{password}"'))
def log_in(login_page: LoginPage, username: str, password: str) -> None:
    login_page.login(username, password)


@then("the inventory page is displayed")
def inventory_is_displayed(inventory_page: InventoryPage) -> None:
    inventory_page.expect_loaded()


@then(parsers.parse('the login error contains "{message}"'))
def login_error_is_displayed(login_page: LoginPage, message: str) -> None:
    login_page.expect_error(message)


@when(parsers.parse('I add "{item_name}" to the cart'))
def add_item(inventory_page: InventoryPage, item_name: str) -> None:
    inventory_page.add_item_to_cart(item_name)


@then(parsers.parse("the cart badge shows {count:d} item"))
def cart_badge_shows_count(inventory_page: InventoryPage, count: int) -> None:
    inventory_page.expect_cart_count(count)


@when("I open the shopping cart")
def open_shopping_cart(inventory_page: InventoryPage) -> None:
    inventory_page.open_cart()


@then(parsers.parse('the cart contains "{item_name}"'))
def cart_contains_item(cart_page: CartPage, item_name: str) -> None:
    cart_page.expect_item(item_name)


@when("I start checkout")
def start_checkout(checkout_page: CheckoutPage) -> None:
    checkout_page.start()


@when(parsers.parse('I enter checkout details "{first_name}" "{last_name}" "{postal_code}"'))
def enter_checkout_details(
    checkout_page: CheckoutPage, first_name: str, last_name: str, postal_code: str
) -> None:
    checkout_page.enter_details(first_name, last_name, postal_code)


@when("I continue to the checkout summary")
def continue_to_checkout_summary(checkout_page: CheckoutPage) -> None:
    checkout_page.continue_to_summary()


@when("I continue checkout without entering customer details")
def continue_without_details(checkout_page: CheckoutPage) -> None:
    checkout_page.continue_to_summary()


@then(parsers.parse('the checkout summary contains "{item_name}"'))
def checkout_summary_contains(checkout_page: CheckoutPage, item_name: str) -> None:
    checkout_page.expect_summary_item(item_name)


@then("the order total is displayed")
def order_total_is_displayed(checkout_page: CheckoutPage) -> None:
    checkout_page.expect_total_displayed()


@when("I finish the order")
def finish_order(checkout_page: CheckoutPage) -> None:
    checkout_page.finish_order()


@then("the order confirmation is displayed")
def order_confirmation_is_displayed(checkout_page: CheckoutPage) -> None:
    checkout_page.expect_order_confirmation()


@then(parsers.parse('the checkout error contains "{message}"'))
def checkout_error_is_displayed(checkout_page: CheckoutPage, message: str) -> None:
    checkout_page.expect_error(message)
