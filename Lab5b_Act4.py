from math import *
from random import random
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
print("This program will estimate the value of Pi using the Monte Carlo Method")
print("\n The Monte Carlo Method sets up a ratio of Area of circle over Area of Square which yields pi/4")
print("\n Using the equation x^2+y^2 < 1 we can figure out which points lie in the circle and which dont")
print("\n Using the count of which points fall inside and outside of circle we can get the ratio and multiply it by 4 to estimate the value of pi")
Hit = 0#Variable that keeps track of the points inside the circle
count=0#Variable that keeps track of the points outside the circle
for i in range (100000):
    xVal = random()#Get a random x value between 0 and 1
    yVal = random()#Get a random y value between 0 and 1
    xSquared = xVal**2
    ySquared = yVal**2
    if(xSquared+ySquared)<1:
        Hit += 1#Increases the count of variable that keeps the count for the points in the circle
    count += 1#Increases the count of variable that keeps the count for the points outside of the circle
piEstimate = 4*(Hit/count)
print("\nThe estimated value of Pi is",piEstimate,"\b. \nAnd the actual value of pi is",pi,"\b. \nThe difference between the actual and preducted is",pi-piEstimate)

#Question 1: When the code is run several times at 100,000 iterations the estimated value of pi varies at the hundreths place.
#The value pretty much stays the same other then small variations in the value due to the different set of x and y values chosen randomly.

#Question 2: When n is 100,000 the variations in the answer are really small and this is because the more the number of trials
# the more precise the predicted value of pi will be

#Question 3: When we iterate the code for 1,000,000 times the difference decreases even more and we always get the first two numbers
# after the decimal right if the prediction is rounded correctly to the hundreths place.

# When we iterate the code for 10,000,000 times the code takes a little longer to run then if it was iterated 1,000,000 times.
# Additionally we always get the two digits after the decimal correct.