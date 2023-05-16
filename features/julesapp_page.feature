Feature: Check the Page functionality

  Background:
    Given login: I am a user on jules app page 2

  @test2
  Scenario: Complete task no. 2
    When login: I click on sign up 2
    When login: I verify the sign up page url "https://jules.app/sign-up"
    When login: I click on login 2
    Then login: I verify the login page url "https://jules.app/sign-in"

#    behave -f html -o behave-report.html --tags=test2
