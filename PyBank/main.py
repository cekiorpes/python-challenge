#Modules
import os
import csv

#Lists
Date = []
Profit_Losses = []

#Set path for file
PyBankpath = os.path.join("..","PyBank","Resources","budget_data.csv")

#Open the csv file
with open(PyBankpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        Date.append(row[0])
        Profit_Losses.append(int(row[1]))

    #Find number of months
    months = (len(Date))

    #Net profit/losses - add up profit/losses in row [1]    
    NetTotal = sum(Profit_Losses)

    #Calculate Average Change (total change in profits/change in months)
    AvgChange = (Profit_Losses[85] - Profit_Losses[0])/(months-1)

    #Find the greatest increase and greatest decrease
    ProfitChange = []
    for i in range (1, len(Profit_Losses)):
        ProfitChange.append(Profit_Losses[i]-Profit_Losses[i-1])
        GreatestIncrease = max(ProfitChange)
        GreatestDecrease = min(ProfitChange)
    
    GreatestIncrease_index = ProfitChange.index(GreatestIncrease)
    GreatestDecrease_index = ProfitChange.index(GreatestDecrease)
    
    DateGreatestIncrease = Date[GreatestIncrease_index + 1]
    DateGreatestDecrease = Date[GreatestDecrease_index + 1]
    
Result_summary = ["Financial Analysis\n",
                  "-----------------------------\n",
                  f'Total Months: {(months)}\n',
                  f'Total: ${NetTotal}\n',
                  f'Average Change: ${AvgChange:.2f}\n',
                  f'Greatest Increase in Profits: {DateGreatestIncrease} (${GreatestIncrease:.2f})\n',
                  f'Greatest Decrease in Profits: {DateGreatestDecrease} (${GreatestDecrease:.2f})\n'
                  ]
                  
#Print results
print(*Result_summary, sep="")

#Write text file with results
#Output path
output_path=os.path.join("..","PyBank","Analysis","financial_analysis.txt")

with open(output_path, 'w') as Analysis:
    Analysis.writelines(Result_summary)


