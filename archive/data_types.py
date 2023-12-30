import math
## Simple Data Types:
# Text Type: 	str
# Numeric Types: 	int, float, complex
# Boolean Type: 	bool
# Binary Types: 	bytes, bytearray, memoryview
# None Type: 	NoneType

## Complex Data Types:
# Sequence Types: 	list, tuple, range
# Mapping Type: 	dict
# Set Types: 	set, frozenset


def add_numbers(number1, number2):
    sum = number1 + number2
    return sum

result1 = add_numbers(2, 3)
print(f'sum of numbers is {result1}')

result2 = add_numbers(5, 7)
print(f'my own formatted result is {result2}')