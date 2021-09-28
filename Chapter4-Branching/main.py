some_word = input("enter an 8 character word please")

# takes the 1st, 3rd, 5th, and 7th character
encoded_word = some_word[0] + some_word[2] + some_word[4] + some_word[6]
# adds the 2nd, 4th, 6th, and 8th character
encoded_word += some_word[1] + some_word[3] + some_word[5] + some_word[7]

print(encoded_word)

number = int(input("Enter a number: "))

if number < 0:
    number *= -1
    print("that is a negative number, let me make it positive for you")

# relational operators
# < less than
# <= less than or equal to
# > greater than
# >= greater than or equal to
# == equals
# != not equals

print(number)

guess = int(input("Guess a number 1-100: "))

if guess > 42:
    print("too high!")
elif guess < 42:
    print("too low!")
else:
    print("You guessed it!")

if guess != 42:
    guess = int(input("Guess again! Guess a number 1-100: "))

    if guess > 42:
        print("too high!")
    elif guess < 42:
        print("too low!")
    else:
        print("You guessed it!")

if guess != 42:
    guess = int(input("Guess again! Guess a number 1-100: "))

    if guess > 42:
        print("too high!")
    elif guess < 42:
        print("too low!")
    else:
        print("You guessed it!")


score = int(input("Enter a score 0-100: "))

# mutually exclusive, one and only one will run - chain
if score >= 94:
    print("A")
elif score >= 90:
    print("A-")
elif score >= 87:
    print("B+")
elif score >= 84:
    print("B")
elif score >= 80:
    print("B-")
elif score >= 77:
    print("C+")
elif score >= 74:
    print("C")
elif score >= 70:
    print("C-")
elif score >= 67:
    print("D+")
elif score >= 64:
    print("D")
elif score >= 60:
    print("D-")
else:
    print("F")

# if you are only checking a single value, the variable should go first
if 94 <= score:
    print("A")
if score >= 94:
    print("A")


# nicer looking than the nested version
#if score >= 94:
#    print("A")
#else:
#    if score >= 90:
#        print("A-")


# logical operator
# and
# true and true == true
# true and false == false
# false and true == false
# false and false == false

# or
# true or true == true
# true or false == true
# false or true == true
# false or false == false

# not
# not true == false
# not false == true

if score >= 90 and score < 94:
    print("A-")

# two relationals in a single expressions works in python, not so many other langaues
if 90 <= score < 94:
    print("A-")


x = int(input("Please enter a value for X"))
y = int(input("Please enter a value for Y"))

if x >= 0 and y >= 0:
    print("You are in quad 1")
elif x < 0 and y >= 0:
    print("You are in quad 2")
elif x < 0 and y < 0:
    print("YOu are in quad 3")
#elif x >= 0 and y < 0: - if you are in 1, 2, or 3, you by default must be in 4
else:
    print("You are in quad 4")


name = input("Enter your name: ")

# python is case sensitive when comparing strings
if name == "Eric":
    print("Hi, that's my name too!")
else:
    print(name, "nice to meet you, I'm Eric!")

my_numbers = []
my_numbers.append(int(input("Enter a number")))
my_numbers.append(int(input("Enter a number")))
my_numbers.append(int(input("Enter a number")))

winning_numbers = [3, 2, 1]

if my_numbers == winning_numbers:
    print("You win the daily 3 lotto!")
else:
    print("You lost, thanks for donating your money")

menu = { "Coffee" : 1.25, "Espresso": 2.0 }
item_to_buy = input("What do you want to buy?")

# with dictionaries, in checks for a KEY - not the associated values
if item_to_buy in menu:
    print(item_to_buy, "costs", menu[item_to_buy])
else:
    print("We don't sell that!")

# ended in the middle of 4.9

