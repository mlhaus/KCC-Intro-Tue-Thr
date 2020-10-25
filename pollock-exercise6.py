from helpers import getNum
from random import randint

def randomNumbers(n):
    result = []
    for i in range(int(n)):
        result.append(randint(0, 100))
    return result

def largerThan(numbers, n):
    result = []
    for num in numbers:
        if num > n:
            if not num in result:
                result.append(num)
    print("List of numbers: " + str(numbers))
    result.sort()
    print("Numbers that are greater than " + str(n) + ": " + str(result))

def main():
    howMany = getNum("How many numbers should be in the list?", 1, 10)
    list = randomNumbers(howMany)
    n = getNum("Enter a number to compare the numbers in the list to", 0, 100)
    largerThan(list, n)
  
main()