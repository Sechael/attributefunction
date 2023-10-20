import random
import csv
import math
import tkinter as tk
from tkinter import simpledialog

def get_max_score():
    max_score = simpledialog.askinteger("Input", "Enter the maximum possible score (e.g., 15): ")
    if max_score is None:
        exit_script()
    if max_score >= 3:
        return max_score
    else:
        return get_max_score()

def get_min_score(max_score):
    min_score = simpledialog.askinteger("Input", f"Enter the minimum possible score (e.g., 3 or greater, at least 1 less than the max score {max_score}): ")
    if min_score is None:
        exit_script()
    if min_score >= 3 and min_score < max_score:
        return min_score
    else:
        return get_min_score(max_score)

def get_X():
    X = simpledialog.askinteger("Input", "Enter the number of rows to generate (1 to 100): ")
    if X is None:
        exit_script()
    if 1 <= X <= 100:
        return X
    else:
        return get_X()

def exit_script():
    print("User canceled input. Exiting script.")
    exit()

root = tk.Tk()
root.withdraw()  # Hide the main tkinter window

# Gather user input for max_score
max_score = get_max_score()

# Gather user input for min_score (with a lower limit and 1 less than max_score)
min_score = get_min_score(max_score)

# Define upper and lower bounds for point_pool
lower_bound = 7 * min_score
upper_bound = 7 * max_score

# Gather user input for point_pool within specified range
point_pool = simpledialog.askinteger("Input", f"Enter the point pool ({lower_bound} to {upper_bound}): ")
if point_pool is None:
    exit_script()
while point_pool < lower_bound or point_pool > upper_bound:
    point_pool = simpledialog.askinteger("Input", f"Point pool must be between {lower_bound} and {upper_bound}. Please enter a valid value: ")
    if point_pool is None:
        exit_script()

# Gather user input for X
X = get_X()

def init_array(X):
    array = []
    for _ in range(X):
        # Generate a list with 7 random values that sum to point_pool
        row = random.sample(range(min_score, max_score + 1), 7)
        # Calculate the remaining points
        remaining_points = point_pool - sum(row)
        # Add the remaining points randomly to the existing values
        while remaining_points > 0:
            index = random.randint(0, 6)
            if row[index] < max_score:
                row[index] += 1
                remaining_points -= 1
        # Check if the sum exceeds point_pool and subtract points if needed
        while sum(row) > point_pool:
            index = random.randint(0, 6)
            if row[index] > min_score:
                row[index] -= 1
        # Calculate the average of Dexterity and Intelligence
        average_dex_int = (row[1] + row[3]) // 2
        # Add the average as the 8th column
        row.append(average_dex_int)
        array.append(row)
    return array

array = init_array(X)

root.destroy()

# Define the CSV filename
csv_filename = 'output.csv'

# Define column labels
column_labels = ["STR", "DEX", "CON", "INT", "PERC", "WILL", "CHA", "Initative"]

# Write the data to the CSV file with column labels
with open(csv_filename, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["Row"] + column_labels)
    for i, row in enumerate(array):
        csv_writer.writerow([i + 1] + row)

print(f"Data for {X} rows has been written to {csv_filename}.")