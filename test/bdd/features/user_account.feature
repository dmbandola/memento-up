Feature: Create User Account

    As a User, I want to create a user account.

    Scenario: Create a user account with correct information
    Given I have input the needed information
    When I click the done button  
    Then the system will output a success message

    Scenario: Create a user account with an existing username
    Given I have input an existing username
    When I click the done button  
    Then the system will alert that the username already exists

    Scenario: Create a user account with wrong information
    Given I did not fill all the information needed
    When I click the done button  
    Then the system will alert to input all the information needed
