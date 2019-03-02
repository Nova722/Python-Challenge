#Dependencies
import os
import csv

csvpath = "C:/Users/chris/NUCHI201902DATA1/Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv"

totalMonths = 0
totalRevenue = 0
greatestRevIncDate = "Date1"
greatestRevIncAmt = 0
greatestRevDecDate = "Date2"
greatestRevDecAmt = 0
revInc = []

with open(csvpath, newline='') as csvfile:
  #skip the header row
  csvfile.readline()

  # CSV reader specifies delimiter and variable that holds contents
  csvreader = csv.reader(csvfile, delimiter=',')

  totalMonths = 0
  totalRevenue = 0
  prevRevenue = 0
  greatestRevIncAmt = 0
  greatestRevDecAmt = 0
  totalRevenueChange = 0

#  Each row is read as a row
  for row in csvreader:
      totalRevenue = totalRevenue + int(row[1])
      totalMonths = totalMonths + 1
      revIncrease = int(row[1]) - prevRevenue
      revInc.append(revIncrease)
      prevRevenue =  int(row[1])
      if(revIncrease > greatestRevIncAmt):
          greatestRevIncAmt = revIncrease
          greatestRevIncDate = row[0]

      if(revIncrease < greatestRevDecAmt):
          greatestRevDecAmt = revIncrease
          greatestRevDecDate = row[0]

Avgchangep = round(sum(revInc[1:len(revInc)])/(len(revInc)-1),2)

file = open("Pybank.txt","w+")

#create the output
file.write("Financial Analysis"+ "\n")
file.write("----------------------------"+ "\n")
file.write("Total Months: "+str(totalMonths)+ "\n")
file.write("Total Revenue: $" + str(totalRevenue)+ "\n")
file.write("Average Revenue Change: $"+str(Avgchangep)+ "\n")
file.write("Greatest Increase in Revenue: "+greatestRevIncDate + " ($" + str(greatestRevIncAmt) +")"+ "\n")
file.write("Greatest Decrease in Revenue: "+greatestRevDecDate + " ($" + str(greatestRevDecAmt) +")"+ "\n")

file.close() 
