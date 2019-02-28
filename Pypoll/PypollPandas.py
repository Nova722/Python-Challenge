import numpy as np
import pandas as pd
import xlrd
import os

file = "C:/Users/chris/NUCHI201902DATA1/Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv"
    
df = pd.read_csv(file) #name df
print(df)

##total number of votes
total = df['Voter ID'].count()
print(total) #3521001 total votes

#Check for duplicates
duplicateCheck = df.duplicated('Voter ID', keep = False) #all non-duplicate values will stay as FALSE
totalduplicates = df['Voter ID'].count()
print(totalduplicates) #total FALSE is 3521001 so there were no duplicates

##number of candidates
candidatecount = df['Candidate'].value_counts() #more detailed breakdown of number of votes
print(candidatecount)

##Percentage of all votes
votedf = pd.DataFrame(data=candidatecount) #Create new dataframe
votedf

#add new columns
#votedf.index.name = 'Candidate'
votedf = votedf.rename(columns={votedf.columns[0]: "number of votes" })
votedf['total percentage'] = 0
votedf

#fill in percentage values
votedf['total percentage'] = round(votedf['number of votes'] / total * 100, 0) 
votedf

##The winner of the election based on popular vote
popvote = votedf.loc[votedf['number of votes'].idxmax()]
print(popvote)

WinnerName = popvote.name #variable for winner name

##Make a new file and print
file = open("Pypoll.txt","w+")


file.write("***Election Results***" + "\n")
file.write("------------------------------------------------"+ "\n")
file.write("Total Votes:" + str(total) + "\n")
file.write("------------------------------------------------"+ "\n")
file.write(str(votedf)+ "\n")
file.write("------------------------------------------------"+ "\n")
file.write("Winner:  " + str(WinnerName) + "\n")


file.close() 