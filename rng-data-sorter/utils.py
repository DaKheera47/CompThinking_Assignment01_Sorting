import random
import time
from sorting_algos import merge_sort, quick_sort, selection_sort


def generate_random_number(numDigits, elements):
    # generate a random number with numDigits digits
    # and repeat this process elements times

    # return a list of random numbers
    output_arr = []
    # 10 ** 3 = 1000
    min_num = 10 ** (numDigits - 1)
    # 10 ** 4 = 10000 - 1 = 9999
    max_num = (10**numDigits) - 1

    for _ in range(elements):
        rand_number = random.randint(min_num, max_num)

        # check if the random number is already in the list
        # if it is, generate another random number
        # repeat this process until a unique random number is generated
        while rand_number in output_arr:
            rand_number = random.randint(min_num, max_num)

        output_arr.append(rand_number)

    return output_arr


def time_array_sort(array, sort_type):
    # using time.perf_counter() instead of time.time()
    # as it is more accurate

    # start timer
    start = time.perf_counter()

    if sort_type == "selection":
        sorted_arr, comparisons = selection_sort(array)
    elif sort_type == "merge":
        sorted_arr, comparisons = merge_sort(array)
    elif sort_type == "quick":
        sorted_arr, comparisons = quick_sort(array)

    # end timer
    end = time.perf_counter()
    # calculate time taken to sort array
    time_taken = end - start
    # returning time in milliseconds
    time_taken = time_taken * 1000

    return sorted_arr, comparisons, time_taken
