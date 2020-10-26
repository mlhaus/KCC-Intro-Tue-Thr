

def findGreaterThen(list1, num):
    greaterThen = []
    for i in list1:
        if i > num and i not in greaterThen:
            greaterThen.append(i)
    greaterThen.sort()

print(findGreaterThen)