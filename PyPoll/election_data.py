import csv
import os

# CSV file Path
election_csv = os.path.join(os.path.dirname(__file__), "election_data.csv")

# Initialise variables
total_votes = 0
candidates = {}
winner = ""

# Read the CSV file
with open(election_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    for row in csvreader:
        total_votes += 1
        candidate = row[2]

        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# The analysis text
analysis_output = f"""
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
"""

# Calculate the percentage of votes each candidate won and calculate the winner
max_votes = 0
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    analysis_output += f"{candidate}: {percentage:.3f}% ({votes})\n"
    
    if votes > max_votes:
        max_votes = votes
        winner = candidate

analysis_output += f"-------------------------\nWinner: {winner}\n-------------------------"

# Print the analysis to the terminal
print(analysis_output)

# Export Text file
output_file = os.path.join("election_results.txt")
with open(output_file, "w") as txtfile:
    txtfile.write(analysis_output)

print("Analysis exported to 'election_results.txt'")
