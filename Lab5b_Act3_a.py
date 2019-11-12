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
print("This program will return a sequence of numbers based on a positive integer inputted leading to 1")
print("The number sequence is known as The Collatz conjecture")
inputNum = int(input("Enter a positive integer here:"))
count = 0#Keeps the count of the number of iterations

while(inputNum / 2 != 1):
    print(int(inputNum))
    if(inputNum%2 != 0):
        inputNum = (3*inputNum)+1#If the inputNum/2 does not have a remainder of 0 then it executes the mathematical expression
    else:
        inputNum = inputNum/2#Else it will divide the inputNum by 2
    count += 1#increases the coutn every time the while loop runs
    
print(int(inputNum))#This takes care of the second to last value which will always be 2 since my condition for while loop evaluates to true at 2
count += 1#Increases count outside of while loop as I am performing the calculation outside of while loop
print(int(inputNum/2))#This takes care of the last digit which is 1 by dividing 2 by 2 giving the last value 1 satisfying the Collatz cojecture
count += 1#Increases count for final time
print("It took",count,"iterations to get to 1 using the Collatz conjecture")