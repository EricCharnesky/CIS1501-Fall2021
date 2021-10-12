import random

# left off at 6.8

def convert_fahrenheit_to_celsius(fahrenheit):
    fahrenheit += 50 # passed by copy ,this won't change the orginal
    celsius = fahrenheit - 32
    celsius *= (5/9)
    return celsius

def print_how_are_you():
    print("How are you?")


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


temp_in_f = int(input("enter a temp in F to convert to C"))
temp_in_c = convert_fahrenheit_to_celsius(temp_in_f)
print(f"That temperature in celsius is: {temp_in_c:.2f}")
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

hello = print_hello()

print(hello)