# left off at 7.4

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

e = alphabet[4]

# slice of indexes
letters = alphabet[5:10] # start at index, give me all the characters up to index 10

slow_way_letters = ""
for index in range(5, 10):
    slow_way_letters += alphabet[index]

last_four_letters = alphabet[len(alphabet)-4:len(alphabet)]
last_four_letters = alphabet[len(alphabet)-4:] # the start and end are optional
# omitting the start means start at the beginning, omitting the end means end at the end

first_10_letters = alphabet[:-16] # 16 less than the end

# start, end, skip/stride
every_other_letter = alphabet[::2]

print(every_other_letter)
print(first_10_letters)

print(last_four_letters)

print(letters)

print(f'the first ten letters are {first_10_letters}')
print('the first ten letters are {}'.format(first_10_letters))

if "mon" in 'Pokemon':
    print('Gotta catch em all!')

