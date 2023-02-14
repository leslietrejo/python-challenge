# Import os module
import os
# Import module for csv files 
import csv

# Path to budget data csv file
pyPollcsv = os.path.join("Resources", "election_data.csv")


# Set up variables to create accumulator
totalVotes = 0 
candiNames = {}
candWinner = ""
totCVotes = 0

# Read csv file
with open(pyPollcsv, 'r') as csvFile:
    csvR = csv.reader(csvFile, delimiter =",")

    # skip the first row
    header = next(csvR)

    for row in csvR:
        totalVotes += 1
        cName = row[2]

        if cName not in candiNames:
            candiNames[cName] = 1

        else: 
            candiNames[cName] += 1

        if candiNames[cName] > totCVotes:
            totCVotes = candiNames[cName]
            candWinner = cName


# Print results to terminal
print("Election Results")
print("--------------------------")
print(f"Total Votes: {totalVotes}")
print("--------------------------")

# print for percentage votes
for cName, respecVotes in candiNames.items():
    perVotes = respecVotes / totalVotes * 100
    print(f"{cName}: {perVotes:.3f}% ({respecVotes})\n")
print("--------------------------")
print(f"Winner: {candWinner}")
print("--------------------------")

outputFile = os.path.join("PollAnalysis.txt")


    # Print analysis text file with outputs
with open(outputFile, 'w') as textFile:
    textFile.write("Election Results\n")
    textFile.write("-------------------------\n")
    textFile.write(f"Total Votes: {totalVotes}\n")
    textFile.write("-------------------------\n")

    for cName, respecVotes in candiNames.items():
        perVotes = respecVotes / totalVotes * 100
        textFile.write(f"{cName}: {perVotes:.3f}% ({respecVotes})\n")
    textFile.write("-------------------------\n")
    textFile.write(f"Winner: {candWinner}\n")
    textFile.write("-------------------------\n")
