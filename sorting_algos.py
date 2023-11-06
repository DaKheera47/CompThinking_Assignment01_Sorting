def selection_sort(arr):
    comparisons = 0
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            comparisons += 1
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr, comparisons


def merge_sort(arr):
    comparisons = 0

    def merge(left, right):
        nonlocal comparisons
        merged, i, j = [], 0, 0
        while i < len(left) and j < len(right):
            comparisons += 1
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    if len(arr) > 1:
        middle = len(arr) // 2
        left_half, left_comparisons = merge_sort(arr[:middle])
        right_half, right_comparisons = merge_sort(arr[middle:])
        comparisons += left_comparisons + right_comparisons
        arr = merge(left_half, right_half)
    return arr, comparisons


def quick_sort(arr):
    comparisons = 0

    def partition(low, high):
        nonlocal comparisons
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            comparisons += 1
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick_sort_recursive(low, high):
        nonlocal comparisons
        if low < high:
            pi = partition(low, high)
            quick_sort_recursive(low, pi - 1)
            quick_sort_recursive(pi + 1, high)

    quick_sort_recursive(0, len(arr) - 1)
    return arr, comparisons
