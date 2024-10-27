### Part Four -- your code goes here. 

import random 
numbers = []
for i in range(10):
    random_number = random.randint(1, 100)
    numbers.append(random_number)

print("Original List:", numbers) 

empty = 0
while empty < len(numbers):
    if numbers[empty] % 2 == 0:
        numbers.pop(empty)
    else:
        empty += 1

print('New List:', numbers)
