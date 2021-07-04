#imports

import os
import csv

#read csv
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    count = 0
    total = 0
    for row in csvreader:
#Calculate total number on months included in the dataset
        count = count + 1
#Calculate net total amount of "Profit/Losses" over the entire period
        total = total + float(row[1])

    average = total / count
    print (count)
    print(total)
    print (average)
    

#Calculate average of the changes in "Profit/Losses" over the entire period
#Calculate average of the changes in "Profit/Losses" over the entire period
#Calculate greatest increase in profits (date and amount) over the entire period
#Calculate greatest decrease in losses (date and amount) over the entire period