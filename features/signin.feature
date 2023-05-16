Feature: Check the Signin functionality

  Background:
    Given login: I am a user on the signin page

  @test1
  Scenario: Complete task no. 1
    When login: I fill in an email "a@mail.com"
    When login: I leave the password empty
    When login: I verify the error is displayed
    Then login: I check log in button is disabled

#    behave -f html -o behave-report.html --tags=test1
