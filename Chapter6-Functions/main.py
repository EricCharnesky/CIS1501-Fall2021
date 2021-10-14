import random

temp_in_f = 0


def print_base(top):
    top()
    print(" ||| ")
    print(" ||| ")

def print_star_top():
    print("  *  ")
    print(" *** ")
    print("*****")

def print_dash_top():
    print("  -  ")
    print(" --- ")
    print("-----")

def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * (9/5)
    fahrenheit += 32
    return fahrenheit

def convert_fahrenheit_to_celsius(fahrenheit):
    global temp_in_f # this is bad form, don't do it
    temp_in_f += 50
    celsius = fahrenheit - 32
    celsius *= (5/9)
    return celsius

def print_how_are_you():
    print("How are you?")
   # sum = 10 - using names from the built in scope is generally bad form
   # some_list = [ 10, 20, 30 ]
   # total = sum(some_list)
   # print(total)


def print_hello():
    print("hello there, I'm a computer!")
    print_how_are_you()


def rectangle_area_and_perimeter(length, width):
    area = length * width
    perimeter = length * 2 + width * 2
    return area, perimeter # a single value, the tuple, which just contains more than one thing


# default or optional arguments
def print_triangle(size, character="*"):
    if size % 2 == 0:
        size += 1
    for row_number in range(1, size+1):
        print(character*row_number)


def add_to_list(value, list=None):
    if list is None:
        list = []
    list.append(value)
    return list


def find_largest_value_in_list(some_list):
    # can't reassign, but you can modify mutable objects
    some_list.append(1_000_000)
    largest = some_list[0]
    for item in some_list:
        if item > largest:
            largest = item
    return largest


def zero_out_list(some_list):
    for index in range(len(some_list)):
        some_list[index] = 0

def create_hamburger(bun, meat, *toppings):
    print(f'{meat} on a {bun}')
    if len(toppings) > 0:
        for item in toppings:
            print(item)


create_hamburger("onion", "quarter pounder", "pickles", "onions", "lettuce")
create_hamburger("white", "quarter pounder")

numbers = add_to_list(10)

add_to_list(20, numbers)

other_numbers = add_to_list(42)

print(other_numbers)


print( find_largest_value_in_list(numbers))
print(numbers)

zero_out_list(numbers)
print(numbers)

# you can pass a function by name, without ()
print_base(print_star_top)

# you can assign a function to a variable
temp = convert_fahrenheit_to_celsius
print(temp(10))



temp_in_f = int(input("enter a temp in F to convert to C"))
temp_in_c = convert_fahrenheit_to_celsius(temp_in_f)
print(f"That temperature in celsius is: {temp_in_c:.2f}")
print(f"the new value for temp_in_f is: {temp_in_f}")
print_hello()
print_hello # this is bad, it doesn't call the function

print_triangle(10)
print_triangle(7, "%")

# print_triangle() - this doesn't work "TypeError: print_triangle() missing 1 required positional argument: 'size'"

length = int(input("enter the rectangle length: "))
width = int(input("enter the rectangle width: "))

area_and_perimeter = rectangle_area_and_perimeter(length, width)
print(f'area is: {area_and_perimeter[0]}') # first item in the tuple result
print(f'perimeter is: {area_and_perimeter[1]}') # second item int eh type result

area, perimeter = rectangle_area_and_perimeter(length, width) # unpacking
print(f'area is: {area}') # first item in the tuple result
print(f'perimeter is: {perimeter}') # second item int eh type result

area, perimeter = rectangle_area_and_perimeter( width=width, leghth=length)

hello = print_hello()

print(hello)