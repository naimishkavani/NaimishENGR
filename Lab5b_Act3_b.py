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
print("This code will get an integer from the user and find the sum from 0 to the inputted number and calculate the product from 1 to the number.")
inputNum = int(input("Please enter a number here:"))
Sum = 0
Product = 1
temp = inputNum#Creates another variable that is set to the value of the inputtedNum so I dont have to change the actual input value
#Calculates the Sum of all of the numbers from 0 to inputted Number
while(temp >= 0):
    Sum += temp#Increases the sum by every different digit between 0 and inputted Num
    temp -=1
temp2 = inputNum#Creates another variable that is set to the value of the inputtedNum so I dont have to change the actual inputvalue
#Calculates the Product of all of the numbers from 1 to inputted Number
while(temp2 >=1):
    Product *= temp2 #Calculates the new product of the current number stored in temp2 and the value in Product and sets the new value to Product
    temp2 -= 1

print("The sum of numbers from 0 to",inputNum,"is",Sum)
print("The product of numbers from 1 to",inputNum,"is",Product)