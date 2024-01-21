# Author: Shaheer Sarfaraz, G21011528
# Year 2, Computational Thinking, 11/2023

import matplotlib.pyplot as plt
from utils import generate_random_number, time_array_sort
import os


# --- CONSTANTS ---
# Directory to store the charts
CHARTS_DIR = "./charts/"
SORTED_ARR_DIR = "./sorted_arrays/"
# number of elements in array to test
SIZES = [100, 1000, 10000]
# number of digits in random number
NUMBER_LEN = 6
# width of bars in bar charts
BAR_WIDTH = 0.1
# size of the charts
FIG_SIZE = (10, 5)
# the type of sorting algorithms to test
TYPES_OF_SORTING = ["selection", "merge", "quick"]


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


# Process the sorting of the array, centralised for easier reading
def process_sorting(
    size, array, sort_type, time_data, comparisons_data, SORTED_ARR_DIR
):
    sorted_arr, comps, sort_time = time_array_sort(array.copy(), sort_type)
    time_data[sort_type].append(sort_time)
    comparisons_data[sort_type].append(comps)
    print(f"{sort_type.capitalize()} Sort: {sort_time}ms, {comps} comparisons")

    destination = os.path.join(SORTED_ARR_DIR, f"{sort_type}_{size}.txt")
    with open(destination, "w") as f:
        f.write("\n".join(map(str, sorted_arr)))


# Create charts directory if it doesn't exist
os.makedirs(CHARTS_DIR, exist_ok=True)
# Create sorted arrays directory if it doesn't exist
os.makedirs(SORTED_ARR_DIR, exist_ok=True)
# creating a dictionary of arrays with the defined sizes
allArrays = {size: generate_random_number(NUMBER_LEN, size) for size in SIZES}

# Dictionaries to store time and comparison data
# for each algorithm and array size
# starting with empty arrays
time_data = {"selection": [], "merge": [], "quick": []}
comparisons_data = {"selection": [], "merge": [], "quick": []}

# Process each array size
for size, array in allArrays.items():
    print(f"Array size: {size}")

    # Process each sorting algorithm
    for sort_type in TYPES_OF_SORTING:
        process_sorting(
            size, array, sort_type, time_data, comparisons_data, SORTED_ARR_DIR
        )

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
