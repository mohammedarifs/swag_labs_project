Feature: Checkout
  As a signed-in customer
  I want to enter checkout details
  So that I can review my purchase

  @smoke
  Scenario: Review an order before placing it
    Given I am logged in as "standard_user"
    When I add "Sauce Labs Backpack" to the cart
    When I open the shopping cart
    And I start checkout
    And I enter checkout details "Ada" "Lovelace" "12345"
    Then the checkout summary contains "Sauce Labs Backpack"
    And the order total is displayed
