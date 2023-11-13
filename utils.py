import random
import time
from sorting_algos import merge_sort, quick_sort, selection_sort


def generateRandomNumber(numDigits, elements):
    # generate a random number with numDigits digits
    # and repeat this process elements times
    # return a list of random numbers
    randomNumbers = []
    # 10 ** 3 = 1000
    minNum = 10 ** (numDigits - 1)
    # 10 ** 4 = 10000 - 1 = 9999
    maxNum = (10**numDigits) - 1

    for i in range(elements):
        randomNumber = random.randint(minNum, maxNum)
        randomNumbers.append(randomNumber)

    return randomNumbers


def timeArraySorting(array, sortType):
    # using time.perf_counter() instead of time.time() because it is more accurate
    # start timer
    start = time.perf_counter()

    if sortType == "selection":
        sorted_arr, comparisons = selection_sort(array)
    elif sortType == "merge":
        sorted_arr, comparisons = merge_sort(array)
    elif sortType == "quick":
        sorted_arr, comparisons = quick_sort(array)

    # end timer
    end = time.perf_counter()
    # calculate time taken to sort array
    timeTaken = end - start
    # returning time in milliseconds
    timeTaken = timeTaken * 1000

    return sorted_arr, comparisons, timeTaken
