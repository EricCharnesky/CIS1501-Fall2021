import math


def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True


def difference_of_primes_and_non_primes_through_n( number ):
    difference = 0
    for number in range(1, number+1):
        if is_prime(number):
            difference += number
        else:
            difference -= number
    return difference


def bad_encryption(some_string):
    values = []
    for index in range(len(some_string)):
        values.append(ord(some_string[index]) + index)
    return values


def reverse_bad_encryption( some_list ):
    word = ""
    for index in range(len(some_list)):
        word += chr(some_list[index] - index)
    return word


def ensure_none_of_the_letters_are_in_a_string(letters_to_check_for, string_to_check ):
    for character in letters_to_check_for:
        if character in string_to_check:
            return False
    return True


value = bad_encryption("midterm")
print(value)
print(reverse_bad_encryption(value))


print(difference_of_primes_and_non_primes_through_n(9))


