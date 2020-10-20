<<<<<<< HEAD
def swap(x,y,arr):
    temp = arr[x] # assigns the value at the first index to the variable temp
    arr[x] = arr[y] # assigns the value of the second index to the first index
    arr[y] = temp # assigns the value that was originally in the first index to the second index


random_words = ["cat", "dog", "rabbit", "turtle"]
=======
def swap(position1,position2,arr):
    temp = arr[position1] # assigns the value at the first index to the variable temp
    arr[position1] = arr[position2] # assigns the value of the second index to the first index
    arr[position2] = temp # assigns the value that was originally in the first index to the second index


random_words = ["cat", "dog", "rabbit", "turtle", "snake"]
>>>>>>> 3c4aaf85eb305c0bd77e6647fc839de9503ab3e9
print(random_words)
last_index = str(len(random_words)-1)
i1 = int(input("Enter an index between 0 and " + last_index + " to swap: "))
i2 = int(input("Enter a second index between 0 and " + last_index + " to swap with: "))
swap(i1, i2, random_words)
print(random_words)