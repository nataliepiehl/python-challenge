# Natalie Piehl
# 2022_01_18
# NU Data Science Bootcamp
# Python Homework
# ------------------------------------------------
# Import modules
import os
import csv
from statistics import mean

# Navigate to working directory of script
os.chdir(os.path.dirname(__file__))

# Define path to data
budget_data = os.path.join('Resources', 'budget_data.csv')

# Initialize variables
unique_months = []
profit_loss_net_total = 0
profit_loss_previous = 0
profit_loss_change = []
profit_loss_max = 0
profit_loss_max_month = "NA"
profit_loss_min = 0
profit_loss_min_month = "NA"

# Read in the CSV file
with open(budget_data, 'r') as csvfile:

    # Generate csvreader object
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip heaader
    header = next(csvreader)

    # Loop through the rpws
    for row in csvreader:
        # Define row elements
        month = row[0]
        profit_loss = int(row[1])

        # Update profit/loss net total
        profit_loss_net_total += profit_loss

        # Calculate change in profit/loss
        change = profit_loss - profit_loss_previous
        profit_loss_change.append(change)

        # Add month if not present in list already
        if month not in unique_months:
            unique_months.append(month)

        # Check if max or min and update values as needed
        if change > profit_loss_max:
            profit_loss_max = change
            profit_loss_max_month = month

        if change < profit_loss_min:
            profit_loss_min = change
            profit_loss_min_month = month

        # Update last profit/lost
        profit_loss_previous = profit_loss

# Calculate number of months
number_of_months = len(unique_months)

# Calculate average profit/loss change
profit_loss_average = round(mean(profit_loss_change), 2)

# Generate results files
with open("analysis/results.txt", "w") as file:

    # Write out each row
    file.write("Financial Analysis \n")
    file.write("------------------------------------ \n")
    file.write(f"Total Months: {number_of_months} \n")
    file.write(f"Total: ${profit_loss_net_total} \n")
    file.write(f"Average Change: ${profit_loss_average} \n")
    file.write(f"Greatest Increase in Profits: {profit_loss_max_month} (${profit_loss_max}) \n")
    file.write(f"Greatest Decreases in Profits: {profit_loss_min_month} (${profit_loss_min}) \n")

# Print out results.txt
results = open("analysis/results.txt", 'r')
contents = results.read()
print(contents)
results.close()
