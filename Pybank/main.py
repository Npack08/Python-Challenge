# Import Modules
import os

import csv

# Collect data from the Resources folder
#budget_csv = "C:/Users/Nico/Desktop/python-challenge/Pybank/Resources/budget_data.csv"
budget_csv= os.path.join("Resources","budget_data.csv")

# List variables to store the data
month_total = []
Profit_Loss = []
profit_change = []
month_of_change = []
greatest_increase = ["",0]
greatest_decrease = ["",99999999999]
net_change = 0
net_prev = 0
total_net = 0

#Read CSV file for data
with open(budget_csv, "r") as csvfile:
    csvreader= csv.reader(csvfile, delimiter=",")

    #Read the header row first
    csv_header = next(csvreader)
    first_row = next(csvreader)
    total_net += int(first_row[1])
    net_prev = int(first_row[1]) 

for row in csvreader:
      
        month_total.append(row[0])
        month_total= len(month_total)
        net_change = int(row[1]) - net_prev
        net_prev = int(row[1])
        month_of_change += [row[0]]

        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change
    

        Profit_Loss.append(int(row[1]))
        total = sum(Profit_Loss)
        
# Create a loop to find changes in Profit and Loss
Variable_A = (Profit_Loss[i + 1] - Profit_Loss[i] for i in range(len(Profit_Loss)-1))
Average = sum(Variable_A) / int(len(Profit_Loss))
print(Average)

output = (f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
print(output)



        

     



