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

greatest_increase = 0
greatest_decrease = 0

#Read CSV file for data
with open(budget_csv, "r") as csvfile:
    csvreader= csv.reader(csvfile, delimiter=",")

    #Read the header row first
    csv_header = next(csvreader)
    
    for row in csvreader:
      
        month_total.append(row[0])
        total_months= len(month_total)
        
        Profit_Loss.append(int(row[1]))
        total = sum(Profit_Loss)
        
        greatest_increase = (Profit_Loss[row[1] + 1])
        print(greatest_increase)
        
# Create a loop to find changes in Profit and Loss
    Variable_A = (Profit_Loss[i + 1] - Profit_Loss[i] for i in range(len(Profit_Loss)-1))
    Average = sum(Variable_A) / int(len(Profit_Loss))
    print(Average)






        

     



