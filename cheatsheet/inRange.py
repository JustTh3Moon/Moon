from random import randrange
import time

# Produces a new number in range of the assigned number
def inRange(startNumber):
    numberRange = 10
    numberMin = startNumber - numberRange
    print(f"Given min variable: {numberMin}")
    numberMax = startNumber + numberRange + 1
    print(f"Given max variable: {numberMax}")
    
    # Limits the number to postiives only
    if numberMin < rangeMin:
        numberMin = rangeMin

    if numberMax > rangeMax + 1:
        numberMax = rangeMax + 1

    randNumber = randrange(numberMin - 1, numberMax)
    allPossibilities(numberMin, numberMax)
    print(f"\nThe random number was: {startNumber}")
    return randNumber

def allPossibilities(x, y):
    for i in range(x, y):
        print(i, end = " ")

# Generates a random number inside of the assigned range
rangeMin = 0
rangeMax = 50
randNumber = randrange(rangeMin, rangeMax)

inRange(randNumber)