Feature: Check the Login functionality

  Background:
    Given login: I am a user on jules app page 3

  @test3
  Scenario: Complete task no. 3
    When login: I click on sign up
    When login: I click on personal
    When login: I click on continue
    When login: I input first name "Robert"
    When login: I press enter after first name input
    When login: I input last name "Stanescu"
    When login: I press enter after last name input
    When login: I enter wrong email "wrong.email"
    When login: I verify the error
    When login: I clear wrong email input
    When login: I enter correct email "abc@gmail.com"
    Then login: I verify that the error is not displayed anymore

#    behave -f html -o behave-report.html --tags=test3
