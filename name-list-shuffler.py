# open "FirstNames.txt" and "LastNames.txt" and create a list of names
# randomly shuffle the list and print the results

import random


# loading files into lists
with open("First Names.txt") as f:
    first_names = f.readlines()
with open("lastNames.txt") as f:
    last_names = f.readlines()

# print lengths of lists
print("First Names: ", len(first_names))
print("Last Names: ", len(last_names))

# cleaning up the data
# strip newline characters from lists
first_names = [name.strip() for name in first_names]
last_names = [name.strip() for name in last_names]

# clip to 4000 in both lists
first_names = first_names[:4000]
last_names = last_names[:4000]

# print lengths of lists
print("First Names: ", len(first_names))
print("Last Names: ", len(last_names))

full_names = []

# create full names by randomly combining first and last names
while len(full_names) < 4000:
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    name = first_name + " " + last_name

    full_names.append(name)

# get the longest name and print number of characters
longest_name = max(full_names, key=len)
print("Longest Name: ", longest_name)
print("Length: ", len(longest_name))

# write to fullnames.txt
with open("fullnames.txt", "w") as f:
    for name in full_names:
        f.write(name + "\n")
