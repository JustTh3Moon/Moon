from random import randrange
import time

# Produces a new number in range of the assigned number
def inRange(x):
    numberRange = 10
    rangeMin = x - numberRange
    print(f"Given min variable: {rangeMin}")
    rangeMax = x + numberRange + 1
    print(f"Given max variable: {rangeMax}")
    
    # Limits the number to postiives only
    if rangeMin < 0:
        rangeMin = 0

    if rangeMax > 51:
        rangeMax = 51

    randNumber = randrange(rangeMin - 1, rangeMax)
    allPossibilities(rangeMin, rangeMax)
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