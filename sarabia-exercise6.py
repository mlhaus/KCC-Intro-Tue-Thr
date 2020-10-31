from helpers import getNum
from random import randint


def randomNumbers(n):
  result = []
  for i in range(n):
    result.append(randint(0, 100))
  return result

def largerThan(list, n):
    result = []
    for item in list:
      count += 1
      if item > n:
        if item not in result:
          (result.append(list))
    print("List of numbers " + str(list))
    result.sort
    print("Numbers that are greater than [n]: " + str(result))


def main():

  howMany = getNum("Please enter a number between 10 and 20.", 10, 20)
  list = randomNumbers(howMany)
  n = getNum("Please enter a number between 0 and 100.", 0, 100))
  largerThan(list, n)
  
main()