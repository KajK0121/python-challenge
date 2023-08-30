import csv
import os

# CSV file Path
budget_csv = os.path.join(os.path.dirname(__file__), "budget_data.csv")

# Initialize the Variables
total_months = 0
net_total = 0
prev_profit_loss = 0
change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

# Read the CSV file
with open(budget_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    for row in csvreader:
        date = row[0]
        profit_loss = int(row[1])

        total_months += 1
        net_total += profit_loss

        if total_months > 1:
            change = profit_loss - prev_profit_loss
            change_list.append(change)

            if change > greatest_increase[1]:
                greatest_increase = [date, change]

            if change < greatest_decrease[1]:
                greatest_decrease = [date, change]

        prev_profit_loss = profit_loss

# Calculation for Average Change
average_change = sum(change_list) / len(change_list)

# Prepare the analysis text
analysis_output = f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${net_total}
Average Change: ${average_change:.2f}
Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})
Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})
"""

# Print the analysis to the terminal
print(analysis_output)

# Export the analysis to a text file
output_file = os.path.join("financial_analysis.txt")
with open(output_file, "w") as txtfile:
    txtfile.write(analysis_output)

print("Analysis exported to 'financial_analysis.txt'")
