# write a function to calculate discount on purchase price
# No discount for 100 or less purchase amount
# Between 100 and 500 Rs, apply 5% discount
# Above 500 Rs up to 2000, apply 10%
# Above 2000, apply 15%

def find_max(a, b):
    if a > b:
        print('a is greater')
    elif a == b:
        print('a and b are equal')
    else:
        print('b is greater')

find_max(50, 500)

# def calculate_discount(amount):
#     # no discount when amount less than 100
#     discount = 0
#     if (amount < 100):
#         discount = 0
#     elif (amount >= 100 and amount < 500):
#         # apply 5% discount
#         discount = amount * 5 / 100
#     elif (amount >= 500 and amount < 2000):
#         # apply 10%
#         discount = amount * 10 / 100
#     else:
#         discount = amount * 15 / 100
    
#     return int(discount)

# a = calculate_discount(50)
# b = calculate_discount(100)
# c = calculate_discount(500)
# d = calculate_discount(2000)

# print(f'discounts {a}, {b}, {c}, {d}')