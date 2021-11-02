
def percentage_of_values_within_x_standard_deviations(some_list, deviations_from_mean ):
    mean = sum(some_list) / len(some_list)
    sum_of_differences_squared = 0
    for value in some_list:
        difference_squared = (value - mean)**2
        sum_of_differences_squared += difference_squared
    standard_deviation = (sum_of_differences_squared / len(some_list))**.5
    x_deviations = standard_deviation * deviations_from_mean
    count_of_values_within_x_deviations = 0
    for value in some_list:
        if mean - x_deviations <= value <= mean + x_deviations:
            count_of_values_within_x_deviations += 1
    return count_of_values_within_x_deviations / len(some_list)


def menu(list_of_choices):
    choice = input(f"Pick one of: {list_of_choices}: ")
    while choice not in list_of_choices:
        choice = input(f"Pick one of: {list_of_choices}: ")
    return choice


def scramble(word, skip):
    # sanity check
    if skip <= 1:
        return word

    scrambled_word = ""
    for start_index in range(0, skip):
        for index in range(start_index, len(word), skip):
            scrambled_word += word[index]
    return scrambled_word


for skip in range(2, 12):
    print(scramble("Beef potpie", skip))


choice = menu(['Rock', 'Paper', 'Scissors'])
