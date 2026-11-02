Feature: Invalid and incomplete shopping flows
  As a customer
  I want clear feedback when I provide invalid information
  So that I can correct my details before proceeding

  Scenario: Login with an incorrect password
    Given the Sauce Demo login page is open
    When I log in with username "standard_user" and password "wrong_password"
    Then the login error contains "Username and password do not match"

  Scenario: Checkout cannot continue without required customer information
    Given I am logged in as "standard_user"
    When I add "Sauce Labs Backpack" to the cart
    When I open the shopping cart
    And I start checkout
    And I continue checkout without entering customer details
    Then the checkout error contains "First Name is required"
