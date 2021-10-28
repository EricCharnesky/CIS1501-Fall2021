import math
import random


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


def prime_factorial_plus_odds_minus_evens(number):
    result = 1
    for value in range(number+1):
        if is_prime(value):
            result *= value
        elif value % 2 == 1:
            result += value
        else:
            result -= value
    return result


def bad_hash(some_string):
    hash = 0
    for character in some_string:
        hash += ord(character)

    return hash


def verify_bad_hash( some_string, some_bad_hash ):
    return some_bad_hash == bad_hash(some_string)


def count_of_vowels_sometimes_y(some_string):
    vowel_count = 0
    vowels = 'aeiou'
    for character in some_string:
        if character.lower() in vowels:
            vowel_count += 1
        elif character.lower() == "y" and random.randint(1, 10) % 2 == 1:
            vowel_count += 1
    return vowel_count


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


print(count_of_vowels_sometimes_y("yyyyyyyyyyyy"))


