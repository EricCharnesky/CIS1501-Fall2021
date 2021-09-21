name = input("What's your name?")

first_initial = name[0]
print("your first initial is", first_initial)
print("your first name has", len(name), "letters")

# there is no character at the length index
# indexes go from 0 - up to but NOT including the length
# Eric
# 0123


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

other_name = alphabet[4] + alphabet[17] + alphabet[8] + alphabet[2]

alphabet = 'abcdefghijklmnopqrstuvwxyz'

print(other_name)

friends = ['Larry', 'Vlad', 'Sam']
#friends.append('Larry')
#friends.append('Vlad')
#friends.append('Sam')

print(friends)

friends[0] = 'Lars'

print(friends)

# remove by value
friends.remove('Sam')

print(friends)

#remove by index
friends.pop(0)

print(friends)

friends.append('Luke')

print('Eric has', len(friends), 'friends')
print(friends)

friends.append(100)

friends.append(42.7)

print(friends)

scores = []

scores.append(int(input('Enter the first score: ')))
scores.append(int(input('Enter the second score: ')))
scores.append(int(input('Enter the third score: ')))

print('The max score is:', max(scores))
print('The min score is:', min(scores))
print('The average score is:', sum(scores) / len(scores) )

print(scores.count(100), 'people scored 100')

# will crash if the item isn't in the list
print('The score 85 is at index', scores.index(85))

weird_list = friends + scores

print(weird_list)

unchangeable_list_is_actually_a_tuple = (100, 85, 100)
print(max(unchangeable_list_is_actually_a_tuple))

# sets don't have indexes or a guaranteed order
# a set only allows unique values
unique_numbers = set([100, 99, 95, 97, 95])
print(unique_numbers)

other_notation_set = {1, 2, 3, 5, 8, 13, 21}
print(other_notation_set)

# no order guarantee, keys must be unique
# dictionary - pair of key -> value mappings
students_scores = {'Eric': 100, 'Larry': 95, 'Vlad': 100, 'Luke': 80}

print(students_scores)
                         # my variable name - key of
print('the for Eric is:', students_scores['Eric'])

# to add an item by key / this will also act an as update
students_scores['Sam'] = 100

# can't have duplicate keys
students_scores['Eric'] = 75

print(students_scores)

# removes an item by key
students_scores.pop('Eric')
print(students_scores)


# other notation, it's uglier
del students_scores['Vlad']
print(students_scores)

# int - integers - whole numbers
# float - numbers with decimals
# chr - single character - can take a numeric ( unicode/ascii ) value

# sequence types

 # immutable
  # String - a bunch of characters - use "" or '' to create
  # Tuple ( Toople or Tuhple ) - can hold any types - use () to create them

 # mutable
  # list - order matters, you can append, remove, pop
  # set - order doesn't matter, unique values only
  # dictionary - mapping type, key->value pairs