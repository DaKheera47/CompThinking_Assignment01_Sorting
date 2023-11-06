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
        selection_sort(array)
    elif sortType == "merge":
        merge_sort(array)
    elif sortType == "quick":
        quick_sort(array)

    # end timer
    end = time.perf_counter()

    return end - start


for array in allArrays:
    print(f"Array size: {len(array)}")

    print(f"Selection Sort took {timeArraySorting(array.copy(), 'selection')}s")
    print(f"Merge Sort took {timeArraySorting(array.copy(), 'merge')}s")
    print(f"Quick Sort took {timeArraySorting(array.copy(), 'quick')}s")
    print("\n")
