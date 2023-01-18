import os
import csv

csvpath = os.path.join("Resources","election_data.csv")

# List variables
total_votes= 0
candidate_list = 0
candidate_vote_percentage = []
votes_per_candidate = []
election_winner = []

#Read CSV file for data
with open(csvpath, "r") as csvfile:
    csvreader= csv.reader(csvfile, delimiter=",")

    #Read the header row first
    csv_header = next(csvreader)

for row in csvreader:
# Count all the votes:
    total_votes = total_votes + 1
    print(total_votes)

