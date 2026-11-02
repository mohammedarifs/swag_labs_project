Feature: Place an order
  As a customer
  I want to place an order after reviewing it
  So that I receive confirmation of my purchase

  @smoke
  Scenario: Complete a purchase
    Given I am logged in as "standard_user"
    When I add "Sauce Labs Backpack" to the cart
    When I open the shopping cart
    And I start checkout
    And I enter checkout details "Ada" "Lovelace" "12345"
    And I continue to the checkout summary
    And I finish the order
    Then the order confirmation is displayed
