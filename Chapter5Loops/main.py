from random import randint


# 5.5
names = ['Eric', 'Jasmine', 'Joy', 'Jeb', 'Vivi', 'Journey', 'Jubilee', 'Jack', 'John']

# name is my variable name for the individual name in the names list as we iterate
# can't actually modify immuatable values inside a list
for name in names:
    name = name.upper()
    print(name)

index = 0
while index < len(names):
    name = names[index]
    name = name.upper()
    print(name)
    index += 1

index = 0
while index < len(names):
    # this actually changes the list
    names[index] = names[index].upper()
    print(names[index])
    index += 1

print(names)

alphabet = 'ABCEDEFGHIJKLMNOPQRSTUVWXYZ'
for letter in alphabet:
    print(letter)

index = 0
while index < len(alphabet):
    print(alphabet[index])
    index += 1




classes = {
    'CIS1501': 'CS 1 for Data Scientists'
    , 'CIS2001': 'CS 2 for Data Scientists'
    , 'CIS3500': 'Data Science 1'
    , 'CIS421': 'Massive Data Management'
    }

# using a for loop with a dictionary gives you KEYS
for my_class in classes:
    print(my_class, classes[my_class])


number = 0
while number < 10:

    if number % 2 == 1:
        number += 1
        continue # stops the current loop and jumps to the header to see if it's true
    print(number)
    number += 1

    # generates essentially a tuple of values 0-9 - not including the value you enter
for number in range(10):
    print(number)

# range( optional start value, end value, optional step )

for number in range(10, 20):
    print(number)

for number in range(10, 20, 2):
    print(number)

# not smart enough to figure out a negative step automatically
for number in range(10, 0, -1):
    print(number)

# this is useful for changing what's in the list
for index in range(len(names)):
    names[index] = names[index].title()

print(names)

# for loops can always be replaced by while loops, but not vice versa

for hour in range(24):
    for minute in range(60):
        for second in range(60):
            print(f'{hour:02d}:{minute:02d}:{second:02d}')


number = 0
while number < 10:
    print(number)
    number += 1
else: # only runs if you don't break the loop
    print('loop is done')

# gives both index and value at the same time
for (index, value) in enumerate(names):
    print(f'index {index} : {value}')

practice_count = 1

total_problems = int(input("How many math problems do you want?"))

# gets a random value from 0-10 inclusive

# runs if the expression or value is true
while practice_count <= total_problems:
    first_number = randint(0, 10)
    second_number = randint(0, 10)
    print("Problem number", practice_count, ":", first_number, "+", second_number)
    practice_count += 1
    # at the end of the loop, it goes back and evaluates again

print("practice these, then go have fun")

print("Lets find the GCD of two numbers")

first_number = int(input("enter the first number"))
second_number = int(input("enter the second number"))

while first_number != second_number:
    if first_number > second_number:
        first_number -= second_number
    else:
        second_number -= first_number

print("the GCD is:", first_number)

receipt = int(input("Enter the receipt value to total: "))
total_receipts = 0
count_of_receipts = 0

while receipt != -1:
    total_receipts += receipt
    count_of_receipts += 1
    receipt = int(input("Enter the receipt value to total or -1 to stop: "))


more_to_enter = 'y'
total_receipts = 0
count_of_receipts = 0

while more_to_enter == 'y':
    receipt = int(input("Enter the receipt value to total: "))
    total_receipts += receipt
    count_of_receipts += 1
    more_to_enter = input("Do you have more receipts to enter? y/n")

print("You entered", count_of_receipts, "receipts, for a total of", total_receipts)
print("the average receipt is", total_receipts/count_of_receipts)


current_stock_investment_value = int(input("what's the current value of your stock investments?"))
original_current_stock_investment_value = current_stock_investment_value
year = 1

while year <= 50:
    current_stock_investment_value *= 1.1
    current_stock_investment_value += 100
    print(f"after {year} years, your investment is worth: $ {current_stock_investment_value:,.2f}")
    year += 1

print("just the original $100: ", original_current_stock_investment_value * 1.1**50)



max_number = int(input("How high of a number do you want to guess to?"))

number_to_guess = randint(1, max_number)

count_of_guess = 1
guess = int(input(f"Guess a number 1-{max_number}: "))

while guess != number_to_guess:
    if guess < number_to_guess:
        print("too low!")
    else:
        print("too high!")

    guess = int(input(f"Guess a number 1-{max_number}: "))
    count_of_guess += 1

print("You guessed it in", count_of_guess, "guesses!")


square_size = int(input("Enter the size square to print: "))

row = 1

while row <= square_size:
    # multiplication and strings just repeat the string X times
    print("*" * square_size)
    row += 1

rectangle_height = int(input("Enter the height of the rectangle to print: "))
rectangle_width = int(input("Enter the width of the rectangle to print: "))
row = 1

while row <= rectangle_height:
    # multiplication and strings just repeat the string X times
    print("#" * rectangle_width)
    row += 1

triangle_size = int(input("Enter the size right triangle to print: "))

row = 1

while row <= triangle_size:
    # multiplication and strings just repeat the string X times
    print("*" * row)
    row += 1

# left off at 5.5
