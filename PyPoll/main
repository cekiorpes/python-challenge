#Modules
import os
import csv

#Lists
Khan_votes = 0
Correy_votes = 0
Li_votes = 0
OTooley_votes = 0

#Set path for file
PyPollpath = os.path.join("..","PyPoll","Resources","election_data.csv")

#Open the csv file
with open(PyPollpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    #Count votes for each candidate
    for row in csvreader:
        if row[2] == "Khan":
            Khan_votes += 1
        
        elif row[2] == "Correy":
            Correy_votes += 1

        elif row[2] == "Li":
            Li_votes += 1
        
        elif row[2] == "O'Tooley":
            OTooley_votes += 1

    #Calculate Total Votes
    Total_votes = Khan_votes + Correy_votes + Li_votes + OTooley_votes
    
    #Calculate percent votes for each candidate
    Khan_percent = Khan_votes/Total_votes
    Correy_percent = Correy_votes/Total_votes
    Li_percent = Li_votes/Total_votes
    OTooley_percent = OTooley_votes/Total_votes

Election_summary = ["Election Results" '\n',
                    "-----------------------------\n",
                    f"Total Votes: {Total_votes}\n",
                    "-----------------------------\n",
                    f'Khan: {Khan_percent:.3%} ({Khan_votes})\n',
                    f'Correy: {Correy_percent:.3%} ({Correy_votes})\n',
                    f'Li: {Li_percent:.3%} ({Li_votes})\n',
                    f"O'Tooley: {OTooley_percent:.3%} ({OTooley_votes})\n",
                    "-----------------------------\n"
                    ]

#Find the winner
winner = max(Khan_votes,Correy_votes,Li_votes, OTooley_votes)
if winner == Khan_votes:
    Election_summary.append("Winner: Khan\n",)
elif winner == Correy_votes:
    Election_summary.append("Winner: Correy\n")
elif winner == Li_votes:
    Election_summary.append("Winner: Li\n")
elif winner == OTooley_votes:
    Election_summary.append("Winner: O'Tooley\n")

Election_summary.append("-----------------------------\n")

#Print and write text file with summary
print(*Election_summary, sep="")

#Output path
output_path=os.path.join("..","PyPoll","Analysis","election_results.txt")

with open(output_path, 'w') as Results:
    Results.writelines(Election_summary)
