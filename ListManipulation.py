### Part Three -- your code goes here. 

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
print('list', numbers)
numbers.sort()
print('list v2', numbers)
while 1 in numbers:
    numbers.remove(1)
numbers.append(7)
numbers.append(8)
print('final list', numbers)
