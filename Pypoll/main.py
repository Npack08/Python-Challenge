import os
import csv

csvpath = os.path.join("Resources","election_data.csv")

# List variables
voters_tally = []
candidates = []
Charles = []
Diana = []
Raymon = []

#Read CSV file for data
def new_func(votes_Dian):
    print(votes_Dian)

with open(csvpath, "r") as csvfile:
    csvreader= csv.reader(csvfile, delimiter=",")

    #Read the header row first
    csv_header = next(csvreader)

    for row in csvreader:
# Count all the votes:
        voters_tally.append(row[2])
        vote_total = len(voters_tally) 

# Create a loop to count how many votes each candidate received.
for vote in voters_tally: 
    if vote == "Charles Casper Stockham":
        Charles.append(vote)
        
    elif vote == "Diana DeGette":
        Diana.append(vote)
        
    else:
        Raymon.append(vote)
        
        
votes_Char = len(Charles)   
votes_Dian = len(Diana)   
votes_Ray = len(Raymon)

#Calculate the percent of votes each candidate received
percent_c= round(votes_Char / vote_total * 100,3)
percent_d= round(votes_Dian / vote_total * 100,3)
percent_r= round(votes_Ray / vote_total * 100,3)

print("Election Results")
print("-----------------------")
print(f"Total Votes: {(vote_total)}")
print("--------------------------")
print(f"Charles Casper Stockham: {(percent_c)}% ({(votes_Char)})")
print(f"Diana DeGette: {(percent_d)}% ({(votes_Dian)})")
print(f"Raymon Anthony Doane: {(percent_r)}% ({(votes_Ray)})")
print("-------------------------")


if votes_Char > votes_Dian and votes_Char > votes_Ray:
    winner="Winner: Charles Casper Stockham"
    print(winner)
elif votes_Dian > votes_Char and votes_Dian > votes_Ray:
    winner="Winner: Diana DeGette"
    print(winner)
else:
    winner="Winner: Raymon Anthony Doane"
    print(winner)
print("------------------------------------")



# Transfer this data into the analysis file 
output_file = "Analysis.csv"

# Open the output file
with open(output_file, "w") as csvfile:
    csvwrite=("Election Results\n"
    "-----------------------\n"
    f"Total Votes: {(vote_total)}\n"
    "--------------------------\n"
    f"Charles Casper Stockham: {(percent_c)}% ({(votes_Char)})\n"
    f"Diana DeGette: {(percent_d)}% ({(votes_Dian)})\n"
    f"Raymon Anthony Doane: {(percent_r)}% ({(votes_Ray)})\n"
    "-------------------------\n"
    f"Winner: {(winner)}\n")
    csvfile.write(csvwrite)
