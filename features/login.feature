Feature: Sauce Demo login
  As a customer
  I want to sign in
  So that I can access the product inventory

  @login
  Scenario: Login with valid credentials
    Given the Sauce Demo login page is open
    When I log in with username "standard_user" and password "secret_sauce"
    Then the inventory page is displayed
