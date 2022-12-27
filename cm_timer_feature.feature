Feature: Creating timer by lib time
  Scenario: The program will fall asleep for the time specified by the user
    Given I have the number 3 - it is sleeping time
    When Program will fall asleep with cm_timer and return sleeping time
    Then I expect the result to be same seconds as user specified