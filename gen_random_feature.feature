Feature: Creating a new array with random numbers
  Scenario: A new array will be created from random numbers provided by the user
    Given I have the numbers 10, 1, 3
    When Array get created with gen_random
    Then I expect the result to be array with random numbers 1-3 which set will be [1,2,3]