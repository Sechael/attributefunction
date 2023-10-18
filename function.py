import random
import csv
import math

def init_array(X):
    array = []
    for _ in range(X):
        row = []
        while len(row) < 7:
            pool = list(range(3, 16))
            random.shuffle(pool)
            value = random.choice(pool)
            if sum(row) + value <= 65:
                row.append(value)
        remaining_points = 65 - sum(row)
        while remaining_points > 0:
            index = random.randint(0, 6)
            if row[index] < 15:
                row[index] += 1
                remaining_points -= 1
        # Calculate the average of Dexterity and Intelligence
        average_dex_int = (row[1] + row[3]) // 2
        # Add the average as the 8th column
        row.append(average_dex_int)
        array.append(row)
    return array

X = 20
array = init_array(X)

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

print(f"Data has been written to {csv_filename}.")
