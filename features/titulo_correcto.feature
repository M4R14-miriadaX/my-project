Feature: correct title

 Scenario: web title is correct
   Given Chrome is up
   When redirect to Python web
   Then web title is correct