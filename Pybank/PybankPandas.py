import numpy as np
import pandas as pd
import xlrd
import os

file = "C:/Users/chris/NUCHI201902DATA1/Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv"
    
df = pd.read_csv(file) #name df
print(df)

TotalMonths = len(df.index)
print(TotalMonths)

##Get the total amount of revenue gained in the dataset
Total = df['Profit/Losses'].sum()
print (Total) #Total Profit/Loss is 38382578

##The average of the changes in "Profit/Losses" over the entire period
pd.options.mode.chained_assignment = None 
df1 = pd.DataFrame(data = df) #created a new df in case so I would still have the original 

df1['previous_profit/losses'] = 0 #added a new row for the previous profit/loss

for i in range(len(df1['Date'])-1):
    df1['previous_profit/losses'].iloc[i+1] = df1['Profit/Losses'].iloc[i]

print(df1)  

 #subtract current-previous month to get the change in profit/loss
df1['change in profit/losses'] = df1['Profit/Losses'] - df1['previous_profit/losses']
print(df1)

#Calculate the average change
length = len(df1)
Average_Change = round((sum(df1['change in profit/losses']) - df1['change in profit/losses'].iloc[0])/ (length - 1), 2)
#needed to subtract the first change in profit/loss since we did not have the previous months data
#I also subtracted 1 from the total since we removed that first data point

print(Average_Change) #avg change is -2315.12

##Greatest increase in Profts
Highest_increase_in_Profits = df.loc[df1['change in profit/losses'].idxmax()]
print(Highest_increase_in_Profits) #Feb 2012 1926159

##Greatest decrease in Profts
Highest_decrease_in_Profits = df.loc[df1['change in profit/losses'].idxmin()]
print(Highest_decrease_in_Profits) #Sep 2013 -219616

##Make a new file and print
file = open("Pybank.txt","w+")


file.write("Financial Analysis" + "\n")
file.write("----------------------------"+ "\n")
file.write("Total Months:  " + str(TotalMonths)+ "\n")
file.write("Total:  $" + str(Total)+ "\n")
file.write("Average Change:  $" + str(Average_Change)+ "\n")
file.write("Greatest Increase in Profits:  " + str(Highest_increase_in_Profits[0]) + "($" + str(Highest_increase_in_Profits[3])+ ")"+ "\n")
file.write("Greatest Decrease in Profits:  " + str(Highest_decrease_in_Profits[0]) + "($" + str(Highest_decrease_in_Profits[3])+ ")" +"\n")

file.close() 

