# sorting_algorithms.py


def selection_sort(arr):
    # Iterate over each element in the array
    for i in range(len(arr)):
        # Assume the current position as the minimum
        min_index = i
        # Find the smallest element's index in the remaining array
        for j in range(i + 1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def merge_sort(arr):
    if len(arr) > 1:
        # Find the middle of the array
        middle = len(arr) // 2
        # Dividing the array elements into 2 halves
        left_half = arr[:middle]
        right_half = arr[middle:]

        # Sorting the first half
        merge_sort(left_half)
        # Sorting the second half
        merge_sort(right_half)

        i = j = k = 0

        # Copy data to temp arrays left_half[] and right_half[]
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr


def quick_sort(arr):
    # Helper function for partitioning the array
    def partition(low, high):
        # Select the pivot element
        pivot = arr[high]
        i = low - 1
        # Rearrange the array by putting elements smaller than the pivot
        # on the left and larger on the right
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        # Swap the pivot element with the element at i+1
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    # Main function to perform quicksort
    def quick_sort_recursive(low, high):
        if low < high:
            # pi is partitioning index, arr[pi] is now at right place
            pi = partition(low, high)
            # Recursively sort elements before partition and after partition
            quick_sort_recursive(low, pi - 1)
            quick_sort_recursive(pi + 1, high)

    quick_sort_recursive(0, len(arr) - 1)
    return arr
