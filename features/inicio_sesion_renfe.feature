Feature: start session

 Scenario: start session is required when buying a ticket
   Given Renfe web is up
   When select Madrid as origin
   And select Barcelona as destination
   And select one way
   And select travel date next week
   And find tickets
   Then tickets are shown
   When select one ticket
   Then start session is required
