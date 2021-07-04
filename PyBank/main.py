#imports

import os
import csv

#read csv
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)

    count = 0
    total = 0
    greatest = 0
    least = 0
    for row in csvreader:
#Calculate total number on months included in the dataset
        count = count + 1
#Calculate net total amount of "Profit/Losses" over the entire period
        total = total + float(row[1])
#Calculate greatest increase in profits (date and amount) over the entire period
        if float(row[1]) > greatest:
            greatest = float(row[1])
            greatest_month = row[0]
#Calculate greatest decrease in losses (date and amount) over the entire period
        if float(row[1]) < least:
            least = float(row[1])
            least_month = row[0]
    average = total / count
    print("\nFinancial Analysis")
    print("----------------------")
    print("Total Months: " + str(count))
    print("Total: $" + str(total))
    print("Average Change: $" + str(round(average,2)))
    print("Greatest Increase in Profits: " + greatest_month + "($" + str(greatest) + ")")
    print("Greatest Decrease in Profits: " + least_month + "($" + str(least) + ")")
