#!python3
import math



# Task 1
#The bank calculates the amount of interest you earn using the simple interest formula:
#interest = principal * rate * #days in the month / 365

#Ask the user to enter the amount of their principal, the number of days in the month the rate of interest expressed as a percentage.  Calculate the amount of interest they would be paid.

#example:
#Enter your amount: 100
#Enter the rate: 2.5
#Enter the # of days in the month: 30
#You earned $0.2 interest. 
#(2 points) 

#principal
input_1 = input("Enter your amount")

#rate
input_2 = input("Enter the rate")

#days in the month
input_3 = input("enter the # of days in the month:")



a = int(input_1)
b = float(input_2)
c = int(input_3)

#i dont know how i need to put more time into this
#interest = principal * rate * #days in the month / 365

interest = a * b/100 * c / 365

#days in the month / 365

in3 = round(interest,1)

in3 = str(in3)

print("You earned $" + in3 + " interest.")