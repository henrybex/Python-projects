# -*- coding: utf-8 -*-
"""Dunkin_2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QcRnBiXCmCTuH2tBvTu9Ff9-gLSZ8gei

# **Dunkin Donuts Coffee Assignment 2**

Dunkin Donuts sells several different *types* and *sizes* of coffee products.

Each product must be specified by both a type and a size.  So, any particular product can be represented by a “tuple” with two values in it, such as
('Cappuccino', ‘Small') or ('Iced Coffee', 'Large').

*Quick Definition!* A "tuple" is a data type in Python that stores multiple items separated by commas. As we learned in notebook 3, these items can be accessed using their index numbers.

We will represent the coffee menu with a Python dictionary.  This dictionary holds the prices of the different types and sizes of coffee products.  

This assignment requires you to complete several functions.  Some of these can be used to extract price information from the dictionary.  Some of these can be used to modify price information in the dictionary.

Below, you'll find some starter code and associated prompts.

Each function has an associated "test" for you written below it. When you run your function, these tests will automatically run your function and display your function's output.

We have also provided you with the expected answer, so you can check for yourself if you have written functions that produce the expected answers! All you have to do is run the code block, and compare the printed values your functions produced with the expected values. The values we have provided as expected values are rounded, but we do not expect your functions to produce round numbers.

The values will be printed as numbers, not as dollars - this is to be expected!

## Turning in the Assignment

When you think that you have your code working, download it as a .py file and submit it to GradeScope. You will need to make sure to remove the "Copy of" prefix from the title before doing so. If you do not get full credit, you can revise your code and resubmit it to GradeScope as many times as you like before the due date.

If you have questions about getting your Python code to work, email the TA or the Instructor.  And if you're contacting someone for help with code, it may be helpful to send them a shareable link to your Colab file to go over.  You can also set up a time to go over your assignment in person or over Zoom.
"""

dunkin_menu = {('Coffee', 'Small'): 1.69, ('Coffee', 'Medium'): 2.09, ('Coffee', 'Large'): 2.39, \
               ('Latte', 'Small'): 2.79, ('Latte', 'Medium'): 3.09, ('Latte', 'Large'): 3.79, \
               ('Cappuccino', 'Small'): 2.69, ('Cappuccino', 'Medium'): 2.99, ('Cappuccino', 'Large'): 3.69, \
               ('Macchiato', 'Small'): 3.49, ('Macchiato', 'Medium'): 3.79, ('Macchiato', 'Large'): 4.49, \
               ('Iced Coffee', 'Small'): 2.49, ('Iced Coffee', 'Medium'): 2.79, ('Iced Coffee', 'Large'): 3.09, \
               ('Cold Brew', 'Small'): 2.99, ('Cold Brew', 'Medium'): 3.29, ('Cold Brew', 'Large'): 3.59, \
               ('Iced Latte', 'Small'): 3.29, ('Iced Latte', 'Medium'): 3.79, ('Iced Latte', 'Large'): 4.29, \
               ('Iced Macchiato', 'Small'): 3.99, ('Iced Macchiato', 'Medium'): 4.49, ('Iced Macchiato', 'Large'): 4.99, \
               ('Coffe Coolatta', 'Small'): 2.99, ('Coffe Coolatta', 'Medium'): 3.99, ('Coffe Coolatta', 'Large'): 4.69}

"""The above variable is a **global variable** meaning that it will be accessible throughout the code blocks below.

The first function you will write will be get_price.  It will return the price of a particular product in the menu given the key for that product. It will not in any way modify any existing values or variables.

Input

- menu: A dictionary that holds the full menu of prices.

- key: A tuple of values that specified a particular product in the menu. For instance, ('Coffee', 'Small').

Output

- val: The price in the menu associated with the product specified by key. val is set to 0 if there is no such key in the menu.
"""

def get_price(menu, key):

    val = 0

    # -------------------------------------------------------------------------
    # YOUR CODE GOES HERE
    #

    val = menu[key]


    #
    # END OF YOUR CODE
    # -------------------------------------------------------------------------

    return val

print("What is the price of a SMALL COLD BREW?")
print("Your answer: ", get_price(dunkin_menu, ('Cold Brew', 'Small')))
print("Expected result: 2.99")
print("")

print("What is the price of a LARGE COFFEE?")
print("Your answer: ", get_price(dunkin_menu, ('Coffee', 'Large')))
print("Expected result: 2.39")
print("")

"""This function, set_price, sets the price of a particular product in the menu. It should not return any value - it's only purpose is to set a value, which can then be accessed later.

Input

- menu: The name of a dictionary that holds the full menu of prices.

- key: A tuple of values that specified a particular product in the menu. For instance, ('Coffee', 'Small').

- val: The new price of the product specified by key.

Output

- none
"""

def set_price(menu, key, val):

    # -------------------------------------------------------------------------
    # YOUR CODE GOES HERE
    #
    menu[key] = val

    #
    # END OF YOUR CODE
    # -------------------------------------------------------------------------

    return

print("Set the the price of a SMALL COLD BREW to 2.80.")
set_price(dunkin_menu, ('Cold Brew', 'Small'), 2.80)
print("")

print("Now, what is the price of a SMALL COLD BREW?")
print("Your answer: ", get_price(dunkin_menu, ('Cold Brew', 'Small')))
print("Expected result: 2.80")
print("")

print("Put the the price of a SMALL COLD BREW back to 2.99.")
set_price(dunkin_menu, ('Cold Brew', 'Small'), 2.99)
print("")

"""This function, total_price, calculates the total price of buying every single item on the menu.

You have been provided already with the variable "tot", which you will in some way have to calculate, and then return at the end of your function.

Input

- menu: The name of a dictionary that holds the full menu of prices.

Output

- tot: The total price of buying each specification [**remove specification**] of a certain product.
"""

def get_total_price(menu):

    tot = 0

    # -------------------------------------------------------------------------
    # YOUR CODE GOES HERE
    #
    for item in menu:
        tot += menu[item]
    return tot


    #
    # END OF YOUR CODE
    # -------------------------------------------------------------------------

    return tot

print("How much does it cost to buy one of each of Dunkin Donut's coffee products?")
print("Your answer: ", get_total_price(dunkin_menu))
print("Expected result: 91.73")
print("")

"""  This function, average_price, calculates the average price of all of the items on the menu.

  You have again been given an "ave" variable, which you will calculate and then return.


Input

- menu: The name of a dictionary that holds the full menu of prices.

Output

- ave: The average cost of a product.
"""

def get_average_price(menu):

    ave = 0

    # -------------------------------------------------------------------------
    # YOUR CODE GOES HERE
    #
    ave = get_total_price(menu) / len(menu)

    #
    # END OF YOUR CODE
    # -------------------------------------------------------------------------

    return ave

print("What is the average price of Dunkin Donut's coffee products?")
print("Your answer: ", get_average_price(dunkin_menu))
print("Expected result: 3.40")
print("")