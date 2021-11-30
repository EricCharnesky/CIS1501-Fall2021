def count_down(number):
    if number >= 0:
        print(number)
        count_down(number-1)

def iterative_fib(nth):
    if nth <= 2:
        return 1
    previous = 1
    current = 1
    current_nth = 2
    while current_nth < nth:
        next = previous + current
        previous = current
        current = next
        current_nth += 1
    return current

def fibonacci(nth):
    if nth <= 2:
        return 1
    return fibonacci(nth-1) + fibonacci(nth-2)

def iterative_binary_search(sorted_list, value_to_search_for):
    start_index = 0
    end_index = len(sorted_list) - 1

    while start_index <= end_index:
        mid = (start_index + end_index) // 2
        if value_to_search_for == sorted_list[mid]:
            return mid
        if value_to_search_for < sorted_list[mid]:
            end_index = mid - 1
        else:
            start_index = mid + 1
    return -1

def _binary_search(sorted_list, value_to_search_for, start_index, end_index):
    if start_index > end_index:
        return -1 # not found in list

    mid = (start_index + end_index) // 2
    if value_to_search_for == sorted_list[mid]:
        return mid
    if value_to_search_for < sorted_list[mid]:
        return _binary_search(sorted_list, value_to_search_for, start_index, mid-1)
    else:
        return _binary_search(sorted_list, value_to_search_for, start_index+1, end_index)

def binary_search(sorted_list, value_to_search_for):
    return _binary_search(sorted_list, value_to_search_for, 0, len(sorted_list) - 1)


for value in range(1, 50):
    print(f"{value}: {iterative_fib(value):,}")


values = [ 1, 3, 6, 9, 15, 21, 35 ]

print(iterative_binary_search(values, 7))
for value in values:
    print( f'found {value} at index {iterative_binary_search(values, value)}')

