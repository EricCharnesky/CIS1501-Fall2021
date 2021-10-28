
my_dictionary = { 'somekey' : "someValue", "nextkey": "someValue" }

# set or get
my_dictionary['somekey']

print(my_dictionary)

my_other_dictionary = dict(somekey='somevalue', nextkey='somevalue')
print(my_other_dictionary)

my_ugly_dictionary = dict([('somekey', 'somevalue'), ('nextkey', 'nextvalue')])

print(my_ugly_dictionary)
my_ugly_dictionary.pop('nextkey')
print(my_ugly_dictionary)
del my_ugly_dictionary['somekey']

print(my_ugly_dictionary)


for key in my_dictionary:
    print(key, ":", my_dictionary[key])

    #only checks keys, not value
if 'somekey' in my_dictionary:
    print('found somekey in my dictionary')

print(my_dictionary['somekey'])
print(my_dictionary.get('anotherkey')) # get avoids crashing, you get None back  or an optional default

for associated_value in my_dictionary.values():
    print(associated_value)

for key, value in my_dictionary.items():
    print(key, ":", value)


for key in sorted(my_dictionary.keys()):
    print(key, ":", my_dictionary[key])

gradebook = {}

gradebook['Eric'] = {}

gradebook['Eric']['Quiz 1'] = 10
gradebook['Eric']['Quiz 2'] = 10
gradebook['Eric']['Quiz 3'] = 10
gradebook['Eric']['Project 1'] = 10

gradebook['Jasmine'] = {}

gradebook['Jasmine']['Quiz 1'] = 10
gradebook['Jasmine']['Quiz 2'] = 10
gradebook['Jasmine']['Quiz 3'] = 10
gradebook['Jasmine']['Project 1'] = 10

print(gradebook)

for grade_item in gradebook['Eric']:
    print(grade_item, ":", gradebook['Eric'][grade_item])


numbers = [1, 2, 3, 4, 5]
for number in numbers: # read only
    number+=10
    print(number)


print(numbers)


for index in range(len(numbers)):
    numbers[index] += 10
    print(numbers[index])

print(numbers)

def print_values(some_list):
    some_list = [1,2,3,4,5] # only reassigns the value in the function
    print(some_list)

print_values(numbers) # the function could change the values in place
print(numbers)
print_values(numbers[:]) # slice of start to end - slicing makes a copy

numbers.pop() # removes the list item
numbers.pop(2) # removes the item at index 2
numbers.remove(11) # removes the first value of 1 it finds

numbers.reverse()
numbers.sort()

index_of_12 = numbers.index(12)
print(index_of_12)

for index, value in enumerate(numbers): # the value is still a copy
    print(index, ":", value)

two_dimensional_list = [
    [0, 1, 2],
    [3, 4, 5],
    [7, 8, 9]
]

print(two_dimensional_list)
for row in two_dimensional_list:
    for value in row:
        print(value, end=" ")
    print()

print(two_dimensional_list[1][1])

def print_board(board):
    for row in board:
        print(row)

def is_cats_game(board):
    for row in board:
        if " " in row:
            return False
    return True


def win_by_diagonal(board):
    return board[1][1] != " " and ((board[1][1] == board[0][0] and board[1][1] == board[2][2])
                                   or (board[1][1] == board[2][0] and board[1][1] == board[0][2]))


def win_by_column(board):
    for column_index in range(3):
        if board[0][column_index] != " " \
                and board[0][column_index] == board[1][column_index] \
                and board[0][column_index] == board[2][column_index]:
            return True
    return False


def win_by_row(board):
    for row in board:
        if row[0] != " " and row[0] == row[1] and row[0] == row[2]:
            return True
    return False


def player_won(board):
    return win_by_row(board) or win_by_column(board) or win_by_diagonal(board)


def game_over(board):
    return is_cats_game(board) or player_won(board)

board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "] ]

whose_turn = "X"


while not game_over(board):
    print_board(board)

    print(f"it's {whose_turn}'s turn!")

    row, col = (input("Enter the row/col to place your mark space separated like: 1 1 ")).split()
    while board[int(row)][int(col)] != " ":
        print("You can't go there!")
        row, col = (input("Enter the row/col to place your mark space separated like: 1 1 ")).split()
    board[int(row)][int(col)] = whose_turn

    whose_turn = "X" if whose_turn == 'O' else 'O'

print_board(board)
print("game over!")

numbers = list(range(1, 11))

print(numbers)

# this will crash since we run out of indexes after we remove items - changing the length is risky
#for index in range(len(numbers)):
#    if numbers[index] % 2 == 1:
#        numbers.remove(numbers[index])

for number in numbers: # fails because the items shift
    if number >= 5:
        numbers.remove(number)

print(numbers)

for number in numbers[:]: # looping through a copy prevents the items from shifting as we loop
    if number >= 5:
        numbers.remove(number)

print(numbers)

#                       expression          item    collection                                                  optional if
my_resulting_list = [ int(number) * 2 for number in input("enter a bunch of numbers space separated").split() if int(number) % 2 == 1 ]

print(my_resulting_list)


my_new_list = []
users_input = input("enter a bunch of numbers space separated")
for number in users_input.split():
    if int(number) % 2 == 1:
        my_new_list.append(int(number) * 2)

my_new_list.sort() # modifies the existing list

sorted_list = sorted(my_new_list) # makes a new list