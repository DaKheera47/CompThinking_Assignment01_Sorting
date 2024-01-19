import matplotlib.pyplot as plt
from utils import generateRandomNumber, timeArraySorting
import os


# --- CONSTANTS ---
# Directory to store the charts
CHARTS_DIR = "./charts/"
# number of elements in array to test
SIZES = [100, 1000, 10000]
# number of digits in random number
NUMBER_LEN = 6
# width of bars in bar charts
BAR_WIDTH = 0.1
# size of the charts
FIG_SIZE = (10, 5)


# --- FUNCTIONS ---
# Plot a bar chart based on the data given
def plot_bar(sizes, data, title, ylabel, filename):
    # Initialize a new figure with a predefined size
    plt.figure(figsize=FIG_SIZE)

    # Calculate the positions for each set of bars
    positions = range(len(sizes))

    # Loop through each sorting algorithm's data to plot
    for i, (sort_type, values) in enumerate(data.items()):
        # Offset position for each bar
        bar_positions = [p + BAR_WIDTH * i for p in positions]
        # Plot the bars with the respective data
        plt.bar(
            bar_positions,
            values,
            width=BAR_WIDTH,
            label=f"{sort_type.capitalize()} Sort",
        )

    # Set the title of the bar chart
    plt.title(title)
    # Label for the x-axis & y-axis
    plt.xlabel("Array Size")
    plt.ylabel(ylabel)
    # Set the x-ticks to be at the center of each group of bars
    plt.xticks([p + BAR_WIDTH for p in positions], sizes)
    # Display the legend on the chart
    plt.legend()
    # Enable the grid for better readability
    plt.grid(True)
    # Save the generated bar chart to a file in the chosen directory
    plt.savefig(os.path.join(CHARTS_DIR, filename))
    # Close the plot
    plt.close()


# Plot a line chart based on the data given
def plot_line(sizes, data, title, ylabel, filename):
    # Initialize a new figure with a predefined size
    plt.figure(figsize=FIG_SIZE)

    # Loop through each sorting algorithm's data to plot
    for sort_type, values in data.items():
        # Plot the lines with the respective data
        plt.plot(sizes, values, label=f"{sort_type.capitalize()} Sort")

    plt.title(title)
    # Label for the x-axis & y-axis
    plt.xlabel("Array Size")
    plt.ylabel(ylabel)
    # Display the legend on the chart
    plt.legend()
    # Enable the grid for better readability
    plt.grid(True)
    # Save the generated line chart to a file in the chosen directory
    plt.savefig(os.path.join(CHARTS_DIR, filename))
    # Close the plot
    plt.close()


# Create charts directory if it doesn't exist
os.makedirs(CHARTS_DIR, exist_ok=True)
# creating a dictionary of arrays with the defined sizes
allArrays = {size: generateRandomNumber(NUMBER_LEN, size) for size in SIZES}

# Dictionaries to store time and comparison data
# for each algorithm and array size
# starting with empty arrays
time_data = {"selection": [], "merge": [], "quick": []}
comparisons_data = {"selection": [], "merge": [], "quick": []}

# Loop through all arrays and process them
for size, array in allArrays.items():
    # print current array size
    print(f"Array size: {size}")

    # Selection Sort
    sel_sorted_arr, sel_comparisons, sel_time = timeArraySorting(
        array.copy(), "selection"
    )
    # save time and comparisons data
    time_data["selection"].append(sel_time)
    comparisons_data["selection"].append(sel_comparisons)
    print(f"Selection Sort: {sel_time}ms, {sel_comparisons} comparisons")

    # Merge Sort
    merge_sorted_arr, merge_comparisons, merge_time = timeArraySorting(
        array.copy(), "merge"
    )
    # save time and comparisons data
    time_data["merge"].append(merge_time)
    comparisons_data["merge"].append(merge_comparisons)
    print(f"Merge Sort: {merge_time}ms, {merge_comparisons} comparisons")

    # Quick Sort
    quick_sorted_arr, quick_comparisons, quick_time = timeArraySorting(
        array.copy(), "quick"
    )
    # save time and comparisons data
    time_data["quick"].append(quick_time)
    comparisons_data["quick"].append(quick_comparisons)
    print(f"Quick Sort: {quick_time}ms, {quick_comparisons} comparisons")

    print("\n")

# plot bar chart for all algorithms
plot_bar(
    SIZES,
    time_data,
    "Sorting Time Comparison",
    "Time (ms)",
    "time_comparison_bar.png",
)

# plot line chart for all algorithms
plot_line(
    SIZES,
    time_data,
    "Sorting Time Comparison",
    "Time (ms)",
    "time_comparison_line.png",
)

# remove selection sort from comparisons data
# since it is too slow to let the other algorithms be visible
del time_data["selection"]

# plot the charts again without selection sort to
# see the other algorithms better
plot_bar(
    SIZES,
    time_data,
    "Sorting Time Comparison",
    "Time (ms)",
    "time_comparison_bar_excluding_selection.png",
)

plot_line(
    SIZES,
    time_data,
    "Sorting Time Comparison",
    "Time (ms)",
    "time_comparison_line_excluding_selection.png",
)
