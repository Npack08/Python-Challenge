# Import Modules
import os

import csv

# Collect data from the Resources folder
# budgetcsv = "C:/Users/Nico/Desktop/python-challenge/Pybank/Resources/budget_data.csv"
budget_csv= os.path.join("Resources","budget_data.csv")
# print(budget_csv)

#Read CSV file for data
with open(budget_csv) as csvfile:
    csvreader= csv.reader(csvfile, delimiter=",")

#Read the header row 
    csv_header = next(csvreader)
    print(csv_header)




    

