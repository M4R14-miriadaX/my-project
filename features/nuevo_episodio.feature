Feature: new episode

 Scenario Outline: new episode available
   Given <navegador> is up
   When redirect to <web> web
   And the user clicks One peace link
   Then new episode is not available
   And last episode is <episodio>

   Examples:
    | navegador | web      | episodio |
    | chrome    | AnimeFLV | 999      |