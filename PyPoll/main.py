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
election_data = os.path.join('Resources', 'election_data.csv')

# Initialize variables
total_votes = 0
candidates = {}

# Read in the CSV file
with open(election_data, 'r') as csvfile:

    # Generate csvreader object
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip heaader
    header = next(csvreader)

    # Loop through the rows
    for row in csvreader:
        # Define row elements
        voter = row[0]
        county = row[1]
        candidate = row[2]

        # Update vote counter
        total_votes += 1

        # Update vote counter per candidate
        candidates[candidate] = candidates.get(candidate, 0) + 1

# Define keys and values of candidates dictionary
candidates_keys = list(candidates)
candidates_values = list(candidates.values())
candidates_percentages = [round(votes / total_votes * 100, 3) for votes in candidates_values]

# Determine winner
max_votes = max(candidates_values)
winner_index = candidates_values.index(max_votes)
winner = candidates_keys[winner_index]

# Generate results files
with open("analysis/results.txt", "w") as file:

    # Write out each row
    file.write("Election Results \n")
    file.write("------------------------------------ \n")
    file.write(f"Total Votes: {total_votes} \n")
    file.write("------------------------------------ \n")
    file.write(f"{candidates_keys[0]}: {candidates_percentages[0]}% ({candidates_values[0]}) \n")
    file.write(f"{candidates_keys[1]}: {candidates_percentages[1]}% ({candidates_values[1]}) \n")
    file.write(f"{candidates_keys[2]}: {candidates_percentages[2]}% ({candidates_values[2]}) \n")
    file.write(f"{candidates_keys[3]}: {candidates_percentages[3]}% ({candidates_values[3]}) \n")
    file.write("------------------------------------ \n")
    file.write(f"Winner: {winner} \n")
    file.write("------------------------------------ \n")

# Print out results.txt
results = open("analysis/results.txt", 'r')
contents = results.read()
print(contents)
results.close()