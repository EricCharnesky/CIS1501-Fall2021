size = int(input('what size diamond?'))

if size % 2 == 0:
    size += 1

spaces = size // 2
stars = 1

while stars <= size:
    print('{}{}'.format(spaces * " ", stars * "*"))
    stars += 2
    spaces -= 1
stars -= 4
spaces += 2
while stars >= 1:
    print('{}{}'.format(spaces * " ", stars * "*"))
    stars -= 2
    spaces += 1


numbers = []
more_to_enter = 'y'
while more_to_enter.lower() == 'y':
    number = int(input("enter a number: "))
    numbers.append(number)
    more_to_enter = input("Do you have more numbers to enter? y/n").lower()

average = sum(numbers) / len(numbers)

total_difference_squareds = 0
for number in numbers:
    total_difference_squareds += (number - average)**2
variance = total_difference_squareds / len(numbers)
standard_deviation = variance**.5

count_of_numbers_within_1_standard_deviation = 0
count_of_numbers_within_2_standard_deviation = 0
count_of_numbers_within_3_standard_deviation = 0

for number in numbers:
    if average - standard_deviation <= number <= average + standard_deviation:
        count_of_numbers_within_1_standard_deviation += 1
        count_of_numbers_within_2_standard_deviation += 1
        count_of_numbers_within_3_standard_deviation += 1
    elif average - 2 * standard_deviation <= number <= average + 2 * standard_deviation:
        count_of_numbers_within_2_standard_deviation += 1
        count_of_numbers_within_3_standard_deviation += 1
    elif average - 3 * standard_deviation <= number <= average + 3 * standard_deviation:
        count_of_numbers_within_3_standard_deviation += 1

print(f"Average: {average} - Standard Deviation: {standard_deviation}")
print(f"There are {count_of_numbers_within_3_standard_deviation / len(numbers) * 100:.0f}% of numbers within 3 standard deviations")
print(f"There are {count_of_numbers_within_2_standard_deviation / len(numbers) * 100:.0f}% of numbers within 2 standard deviations")
print(f"There are {count_of_numbers_within_1_standard_deviation / len(numbers)* 100:.0f}% of numbers within 1 standard deviations")