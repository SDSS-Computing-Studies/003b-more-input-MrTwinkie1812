#!python3
"""
Assignment: Exchange rate
The current exchange rate is 1.25 CAD per 1 USD
Create a program that asks the user for the number of Canadian Dollars they have
and then have the program display how many USD that is equivalent to:
You may need to use rounding or decimal formatting


example
How many Canadian Dollars do you have? 10
That is worth $8.00 USD

How many Canadian Dollars do you have? 1.25
That is worth $1.00 USD
"""
input_1 = input("Enter the population:")
input_2 = input("Enter the rate of growth in percent:")
input_3 = input("Enter the number of days:")


a = int(input_1) 
b = int(input_2)
c = int(input_3)


interest = a * b * c
#days in the month / 365
interest = str(interest)
print(interest)
input_4 = input("There will be"+ interest +"people after"+ c +" days")
