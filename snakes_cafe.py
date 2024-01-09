intro_menu = """
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
"""

order = {
  'appetizers': {
    'Wings': 0,
    'Cookies': 0,
    'Spring Rolls': 0
  }, 
  'entrees': {
    'Salmon': 0,
    'Steak': 0,
    'Meat Tornado': 0,
    'A Literal Garden': 0
  },
  'desserts': {
    'Ice Cream': 0,
    'Cake': 0,
    'Pie': 0
  },
  'drinks': {
    'Coffee': 0,
    'Tea': 0,
    'Unicorn Tears': 0
  }
}

def handle_order_input(order_input):

  if order_input == 'Quit':

    return 'quit'
  
  else:

    for course in order:
      if order_input in order[course]:

        order[course][order_input] += 1
        quantity = order[course][order_input]

        order_statement = f'{quantity} {"order" if quantity == 1 else "orders"} of {order_input} {"has" if quantity == 1 else "have"} been added to your meal'
        response = f'\n ** {order_statement} ** \n'
        
        return response
      
  return '\n ** Not Found on the Menu; Check Spelling ** \n'

print(intro_menu)

order_input = ''
while order_input.lower() != 'quit':
  
  order_input = input('> ')
  order_input = order_input.title()

  response = handle_order_input(order_input)

  if response != 'quit':
    print(response)