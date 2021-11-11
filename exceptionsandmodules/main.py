# import by module name ( python file name )
import random

from mug import Mug

from random import randint

# from a file, import functions or classes by name
from mystuff import add

random.randint(1, 9)
randint(0,10)
add(1,2)

is_invalid_number = True
while is_invalid_number:

    try: # an exception might happen, get ready to handle it
        number = int(input("enter a number 1-10"))
        is_invalid_number = False
    except ValueError as e: # handle the exception and don't crash
        print(e)

print(number* 10)


coffee_mug = Mug(300, "blue")
try:
    coffee_mug.fill()
    how_much_to_drink = int(input("How many milliters do you want to drink?"))
    coffee_mug.drink(how_much_to_drink)
except ValueError as e:
    print(e)