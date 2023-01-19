# Import Modules
import os

import csv

# Collect data from the Resources folder
#budget_csv = "C:/Users/Nico/Desktop/python-challenge/Pybank/Resources/budget_data.csv"
budget_csv= os.path.join("Resources","budget_data.csv")

# List variables to store the data
month_total = []
Profit_Loss = []
month_of_change = []
greatest_increase = ["",0]
greatest_decrease = ["",99999999999]
net_change = 0
total = 0

#Read CSV file for data
with open(budget_csv, "r") as csvfile:
    csvreader= csv.reader(csvfile, delimiter=",")

    #Read the header row first
    first_row = next(csvreader)
    first_row_data = next(csvreader)
    net_prev = int(first_row_data[1])
    total += int(first_row_data[1])
    month_total.append(first_row_data[0])

# Loop through the variable list
    for row in csvreader:
        month_total.append(row[0])
        total_months = len(month_total) 
        total += int(row[1])
        net_change = int(row[1]) - net_prev
        net_prev = int(row[1])
        month_of_change += [row[0]]
        Profit_Loss.append(net_change)
       

        # Create an if statement to calculate the greatest increase and decrease in profit
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change
    
    
# Create a loop to find average change in Profit and Loss
Variable_A = [Profit_Loss[i + 1] - Profit_Loss[i] for i in range(len(Profit_Loss)-1)]
Average = round(sum(Profit_Loss) / len(Profit_Loss),2)


output = (f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print results

print("Financial Analysis")
print("------------------------")
print(f"Total Months:  {total_months}")
print(f"Total: ${total}")
print(f"Average Change: $({Average})")
print(output)

#Set variable for output file
# Transfer this data into the analysis file 

output_file = "Analysis.csv"

# Write the result to the Analysis.csv
with open(output_file, "w") as csvfile:
    csvwrite=("Financial Analysis\n"
    "-----------------------\n"
    f"Total Months:  {total_months}\n"
    f"Total: ${total}\n"
    f"Average Change: $({Average})\n"
    f"{output}")
    csvfile.write(csvwrite)


        

     



