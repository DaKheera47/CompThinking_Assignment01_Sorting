import time
import matplotlib.pyplot as plt
from utils import generateRandomNumber, timeArraySorting

# Directory where the charts will be saved
import os

CHARTS_DIR = "./charts/"
os.makedirs(CHARTS_DIR, exist_ok=True)

sizes = [100, 1000, 10000]
allArrays = {size: generateRandomNumber(6, size) for size in sizes}

# Dictionaries to store time and comparison data for each algorithm and array size
time_data = {"selection": [], "merge": [], "quick": []}
comparisons_data = {"selection": [], "merge": [], "quick": []}
# time_data = {"merge": [], "quick": []}
# comparisons_data = {"merge": [], "quick": []}

for size, array in allArrays.items():
    print(f"Array size: {size}")

    # Selection Sort
    selection_sorted_arr, selection_comparisons, selection_time = timeArraySorting(
        array.copy(), "selection"
    )
    time_data["selection"].append(selection_time)
    comparisons_data["selection"].append(selection_comparisons)
    print(f"Selection Sort: {selection_time}ms, {selection_comparisons} comparisons")

    # Merge Sort
    merge_sorted_arr, merge_comparisons, merge_time = timeArraySorting(
        array.copy(), "merge"
    )
    time_data["merge"].append(merge_time)
    comparisons_data["merge"].append(merge_comparisons)
    print(f"Merge Sort: {merge_time}ms, {merge_comparisons} comparisons")

    # Quick Sort
    quick_sorted_arr, quick_comparisons, quick_time = timeArraySorting(
        array.copy(), "quick"
    )
    time_data["quick"].append(quick_time)
    comparisons_data["quick"].append(quick_comparisons)
    print(f"Quick Sort: {quick_time}ms, {quick_comparisons} comparisons")

    print("\n")


def plot_bar(sizes, data, title, ylabel, filename):
    plt.figure(figsize=(10, 5))

    bar_width = 0.1  # Width of the bars
    positions = range(len(sizes))  # Bar positions

    for i, (sort_type, values) in enumerate(data.items()):
        plt.bar(
            [p + bar_width * i for p in positions],
            values,
            width=bar_width,
            label=f"{sort_type.capitalize()} Sort",
        )

    plt.title(title)
    plt.xlabel("Array Size")
    plt.ylabel(ylabel)
    plt.xticks([p + bar_width for p in positions], sizes)
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(CHARTS_DIR, filename))
    plt.close()


def plot_line(sizes, data, title, ylabel, filename):
    plt.figure(figsize=(10, 5))
    for sort_type, values in data.items():
        plt.plot(sizes, values, label=f"{sort_type.capitalize()} Sort")

    plt.title(title)
    plt.xlabel("Array Size")
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(CHARTS_DIR, filename))
    plt.close()


plot_bar(
    sizes,
    time_data,
    "Sorting Time Comparison",
    "Time (ms)",
    "time_comparison_bar.png",
)

plot_line(
    sizes, time_data, "Sorting Time Comparison", "Time (ms)", "time_comparison_line.png"
)

# remove selection sort from comparisons data
del time_data["selection"]

print("Time Data")
print(time_data)

plot_bar(
    sizes,
    time_data,
    "Sorting Time Comparison",
    "Time (ms)",
    "time_comparison_bar_excluding_selection.png",
)

plot_line(
    sizes,
    time_data,
    "Sorting Time Comparison",
    "Time (ms)",
    "time_comparison_line_excluding_selection.png",
)
