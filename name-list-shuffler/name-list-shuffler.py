# Author: Shaheer Sarfaraz, G21011528
# Year 2, Computational Thinking, 11/2023

import random

MAX_NAMES = 4000
# character to go between first and last name
NAME_DELIMITER = " "
FIRST_FILE_NAME = "First Names.txt"
LAST_FILE_NAME = "lastNames.txt"

# loading files into lists
with open(FIRST_FILE_NAME) as f:
    first_names = f.readlines()
with open(LAST_FILE_NAME) as f:
    last_names = f.readlines()

# print number of names read
print(f"Number of first names read: {len(first_names)}")
print(f"Number of last names read: {len(last_names)}")

# clip to MAX_NAMES in both lists
first_names = first_names[:MAX_NAMES]
last_names = last_names[:MAX_NAMES]

# cleaning up the data
# strip newline characters from lists
first_names = [name.strip() for name in first_names]
last_names = [name.strip() for name in last_names]

# empty list to store full names
full_names = []
while len(full_names) < MAX_NAMES:
    # choose random first and last name
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)

    # create full name by combining first and last name with delimiter
    name = f"{first_name}{NAME_DELIMITER}{last_name}"

    # don't add if duplicate
    if name in full_names:
        continue

    # add to list if not duplicate
    full_names.append(name)

# key is the function that is used to determine the max
# so in our case we want to use the length of the string
longest_name = max(full_names, key=len)
print("Longest Name: ", longest_name)
print("Length: ", len(longest_name))

with open("fullnames.txt", "w") as f:
    # write each name on a new line
    f.write("\n".join(full_names))
