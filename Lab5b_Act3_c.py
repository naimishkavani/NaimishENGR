from math import *

"""
# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Naimish Kavani
# Section: 512
# Assignment: Lab Assignment 5
# Date: 10/03/2019
"""

print("This program will tell you which numbers are prime and not prime between 2 and 100 inclusive")
count = 0
startNum = 2
#The while loop below finds out which numbers from 2 to 100 are prime and not prime and print out the results
while(startNum <= 100):
    for i in range(2,startNum):
        if(startNum%i)==0:
            print(startNum,"is not Prime")
            break#This breaks the loop because if the startNum is classified as not Prime then no need to keep checking it
    else:
        print(startNum,"is Prime")
        count += 1#Keeps the count of the number of prime numbers between 2 and 100 inclusive
    startNum += 1
print("There are",count,"number of primes between 2 and 100")
