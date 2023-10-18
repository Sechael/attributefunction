import random
import csv
import math

# Define the maximum and minimum possible scores and point pool
max_score = 15
min_score = 3
point_pool = 65

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

X = 10  # You can change the number of rows as needed
array = init_array(X)

# Define the CSV filename
csv_filename = 'output.csv'

# Define column labels
column_labels = ["STR", "DEX", "CON", "INT", "PERC", "WILL", "CHA", "Average"]

# Write the data to the CSV file with column labels
with open(csv_filename, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["Row"] + column_labels)
    for i, row in enumerate(array):
        csv_writer.writerow([i + 1] + row)

print(f"Data for {X} rows has been written to {csv_filename}.")
