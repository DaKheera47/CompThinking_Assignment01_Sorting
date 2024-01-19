def selection_sort(arr):
    # Initialize the number of comparisons
    comparisons = 0

    # Traverse through all array elements
    for i in range(len(arr)):
        # Find the minimum element in remaining unsorted array
        min_index = i

        for j in range(i + 1, len(arr)):
            # Increment the comparison counter
            comparisons += 1

            # If the curr element is smaller than the min element
            # change min_index
            if arr[min_index] > arr[j]:
                min_index = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr, comparisons


def merge(left, right):
    # Initialize the merged list and comparison counter
    merged = []
    comparisons = 0
    i, j = 0, 0

    while i < len(left) and j < len(right):
        # Increment the comparison counter
        comparisons += 1

        # If the left element is smaller than the right element
        if left[i] < right[j]:
            # Append the left element to 'merged'
            merged.append(left[i])
            i += 1
        else:
            # Append the right element to 'merged'
            merged.append(right[j])
            j += 1

    # Append any remaining elements of 'left' and 'right' to 'merged'
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged, comparisons


def merge_sort(arr):
    # If array is larger than 1, proceed to split and merge
    if len(arr) > 1:
        # Find the middle of the array using floor division
        middle = len(arr) // 2

        # Recursively split and merge sort each half
        left, left_comps = merge_sort(arr[:middle])
        right, right_comps = merge_sort(arr[middle:])

        # Merge the sorted halves and add up comparisons
        merged, merge_comps = merge(left, right)
        total_comps = left_comps + right_comps + merge_comps

        return merged, total_comps
    else:
        # If the array is a single element, return it as is with 0 comparisons
        return arr, 0


def partition(arr, low, high):
    # Choose the pivot element
    pivot = arr[high]
    # Initialize the smaller element index
    i = low - 1
    comparisons = 0

    for j in range(low, high):
        # Compare against the pivot
        comparisons += 1

        if arr[j] < pivot:
            i += 1
            # If current element is smaller than the pivot
            # swap it with the element at index i
            arr[i], arr[j] = arr[j], arr[i]

    # Swap the pivot element to the correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    # Return the partitioning index and comparisons
    return i + 1, comparisons


def quick_sort_recursive(arr, low, high):
    # Total comparisons starts at zero
    total_comparisons = 0

    if low < high:
        # Partition the array and get the pivot index
        pi, comparisons = partition(arr, low, high)
        total_comparisons += comparisons

        # Sort the elements before and after the partition
        total_comparisons += quick_sort_recursive(arr, low, pi - 1)
        total_comparisons += quick_sort_recursive(arr, pi + 1, high)

    return total_comparisons


def quick_sort(arr):
    # Call the quick sort recursive function and track comparisons
    total_comparisons = quick_sort_recursive(arr, 0, len(arr) - 1)

    return arr, total_comparisons
