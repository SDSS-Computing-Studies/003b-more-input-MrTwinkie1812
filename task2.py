#!python3
import math

#A population can be modeled by the following:
#future population = (current population)*(1+r)^(time in years) 
#Have the user enter the current population, the rate of growth as a decimal and the number of DAYS.
#Calculate the expected future population


#Enter the population: 25000000


#Enter the rate of growth in percent: 2.1


#Enter the number of days: 12


#There will be 25017087 people after 12 days


#current population
input_1 = input("Enter the population:")

#1+rate
input_2 = input("Enter the rate of growth in percent:")

#time in years 0.0328767
input_3 = input("Enter the number of days:")


a = int(input_1) 
b = float(input_2)
c = float(input_3)


interest = a * b / 100 * c / 365
#days in the month / 365
interest = str(interest)


in3 = round(interest,1)



#future population = (current population)*(1+r)^(time in years) 
print ("There will be "+ in3 +" people after 12 days")