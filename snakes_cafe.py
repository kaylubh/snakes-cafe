print("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
""")

order = {
  appetizers: {

  }, 
  entrees: {
    
  },
  desserts: {
    
  },
  drinks: {
    
  }
}

order_input = ''
while order_input.lower() != 'quit':
  order_input = input('> ')