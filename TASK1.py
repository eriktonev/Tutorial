import random

numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}#has to be set or sequence
numbers_to_output = 9#how many numbers to add to the new lists

random_numbers = random.sample(numbers, numbers_to_output)

print(random_numbers)