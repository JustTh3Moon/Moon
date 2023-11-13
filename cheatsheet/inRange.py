from random import randrange
import time

# Produces a new number in range of the assigned number
def inRange(x):
    numberRange = 10
    xMin = x - numberRange
    print(f"Given min variable: {xMin}")
    xMax = x + numberRange + 1
    print(f"Given max variable: {xMax}")
    
    # Limits the number to postiives only
    if xMin < rangeMin:
        xMin = rangeMin

    if xMax > rangeMax + 1:
        xMax = rangeMax + 1

    randNumber = randrange(xMin - 1, xMax)
    allPossibilities(xMin, xMax)
    print(f"\nThe random number was: {x}")
    return randNumber

def allPossibilities(x, y):
    for i in range(x, y):
        print(i, end = " ")

# Generates a random number inside of the assigned range
rangeMin = 0
rangeMax = 50
randNumber = randrange(rangeMin, rangeMax)

inRange(randNumber)