# Created by anooppottammal at 11/7/24
Feature: contact us page functionality

#  Scenario: User can open the Contact us page
#    Given Open reely main page
#    When  Log in to the page
#    When  Click on settings option
#    When  Click on Contact us option
#    When  Verify contact us page opened
#    Then  Verify there are at least 4 social media icons
#    Then  Verify “Connect the company” button is available and clickable
  # Enter feature description here

  Scenario: User can open the Contact us page
    Given Open reely main page
    When  Log in to the page
    When  Click on main menu
    When  Click on profile icon
    When  Click on Contact us
    When  Verify contact us page opened
    Then  Verify there are at least 4 social media icons
    Then  Verify “Connect the company” button is available and clickable