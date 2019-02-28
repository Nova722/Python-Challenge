import os
import csv

file = "C:/Users/chris/NUCHI201902DATA1/Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv"

#Create variables   
votetotal = 0
listofcandidates = []
votecount = []

#open csv run a forloop for totals needed
with open(file, newline='') as csvfile:
    csvfile.readline()
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        votetotal = votetotal+1
        candidate = row[2]
        if not candidate in listofcandidates:
            listofcandidates.append(candidate)
            votecount.append(1)
        else:
            candidateindex =  listofcandidates.index(candidate)
            curVoteTally = votecount[candidateindex]
            votecount[candidateindex] = curVoteTally+1
                        

##Make a new file and print
file = open("Pypoll(standard Printout).txt","w+")
lines = []
file.write("Election Results"+ "\n")
file.write("-------------------------"+ "\n")
file.write("Total Votes: "+str(votetotal)+ "\n")
file.write("-------------------------"+ "\n")
winningVotes = 0
for candidate in listofcandidates:
    votes = votecount[listofcandidates.index(candidate)]
    pctVotes = (votes/votetotal)*100
    if votes > winningVotes:
        winner = candidate
        winningVotes = votes
    file.write(candidate+": "+str(round(pctVotes,2))+"% "+"("+str(votes) +")"+ "\n")
file.write("-------------------------"+ "\n")
file.write("Winner: "+winner+ "\n")
for line in lines:
    print(line)
    print(line,file=file)
file.close()  

