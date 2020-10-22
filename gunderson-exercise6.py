from helpers import getNum
from random import randint

def randomNumbers(num):
    result = []
    count = 0
    while count < num:
        result.append(randint(0, 100))
        count += 1
    return result


def largerThan(numArr, numSingle):
    result = []
    for item in numArr:
        if item > numSingle:
            if item not in result:
                result.append(item)
    print('List of numbers:', numArr)
    result.sort()
    print('Numbers that are greater than ', numSingle, ': ', result, sep='')
    



def main():
    howMany = getNum('Please enter a number between 10 and 20:', 10, 20)
    list = randomNumbers(howMany)
    n = getNum('Please enter a number between 0 and 100:', 0, 100)
    largerThan(list, n)

  
main()