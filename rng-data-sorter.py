# a) Create three random arrays with the following sizes: 100, 1,000, and 10,000 elements. These arrays will simulate real-world datasets. Each generated number should have 6 digits ranging from 100,000 to 999,999.
# b) Implement all three sorting algorithms: Selection Sort, Merge Sort, and QuickSort.
# c) Apply each sorting algorithm to the three arrays separately. Ensure that you are sorting copies of the original arrays to maintain data integrity.

import time

from sorting_algos import merge_sort, quick_sort, selection_sort
from utils import generateRandomNumber

sizes = [100, 1000, 10000]
allArrays = []

# generate random arrays of sizes in sizes array
for size in sizes:
    array = generateRandomNumber(6, size)
    allArrays.append(array)


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


for array in allArrays:
    print(f"Array size: {len(array)}")

    selection_sorted_arr, selection_comparisons, selection_timeTaken = timeArraySorting(
        array.copy(), "selection"
    )
    print(
        f"Selection Sort took {selection_timeTaken}ms, {selection_comparisons} comparisons"
    )

    merge_sorted_arr, merge_comparisons, merge_timeTaken = timeArraySorting(
        array.copy(), "merge"
    )
    print(f"Merge Sort took {merge_timeTaken}ms, {merge_comparisons} comparisons")

    quick_sorted_arr, quick_comparisons, quick_timeTaken = timeArraySorting(
        array.copy(), "quick"
    )
    print(f"Quick Sort took {quick_timeTaken}ms, {quick_comparisons} comparisons")

    print("\n")
