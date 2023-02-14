# Import os module
import os
# Import module for csv files 
import csv

# Path to budget data csv file
pyBankcsv = os.path.join("Resources", "budget_data.csv")


# Set up variables to create accumulator
totalMonths = 0 
profitTotal = 0
netChange = 0
prevChange = 0
totalChanges = []
averageChange = 0
greatestMax = ["", 0]
greatestMin = ["", 999999999]

# Read csv file
with open(pyBankcsv, 'r') as csvFile:
    csvR = csv.reader(csvFile, delimiter =",")

    # skip the first row
    header = next(csvR)

    # loop through rows to find total months
    for row in csvR:
        totalMonths += 1 
        profitTotal += int(row[1])

        # loop to keep track of net changes and add to total
        if totalMonths > 1:
            netChange = int(row[1]) - prevChange 
            totalChanges.append(netChange)
        prevChange = int(row[1])

        # conditionals to find Greatest Increase and Decrease
        if netChange > greatestMax[1]:
            greatestMax[0] = row[0]       
            greatestMax[1] = netChange
        if netChange < greatestMin[1]:
            greatestMin[0] = row[0]
            greatestMin[1] = netChange

    # find Average Change using total amount of changes / observations
    averageChange = sum(totalChanges) / len(totalChanges)  


    # Print results to terminal
    print("Financial Analysis")
    print("--------------------------")
    print(f"Total Months: {totalMonths}")
    print(f"Total: ${netChange}")
    print(f"Averag Change: ${averageChange}")
    print(f"Greatest Increase in Profits: {greatestMax}")
    print(f"Greatest Decrease in Profits: {greatestMin}")


    # Print analysis text file with outputs
    outputFile = os.path.join("Analysis1.txt")

    with open(outputFile, 'w') as textfile:

        textfile.write("Financial Analysis\n")
        textfile.write("--------------------------\n")
        textfile.write(f"Total Months: {totalMonths}\n")
        textfile.write(f"Total: ${netChange}\n")
        textfile.write(f"Average Change: ${averageChange:.2}\n")
        textfile.write(f"Greatest Increase in Profits): {greatestMax[0]} (${greatestMax[1]})\n")
        textfile.write(f"Greatest Decrease in Profits): {greatestMin[0]} (${greatestMin[1]})\n")       




