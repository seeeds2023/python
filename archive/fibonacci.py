
# This function does...
# input: integer value, valid range 1 to n
# Input values less than one will result in error
def fibbinocci(n):
    if n < 1:
       print(f'invalid input {n}')
       exit(1)
    elif n == 1:
        print(n)
        return

    a = 0
    b = 1
    for i in range(0, n):
     c = a + b
     a = b
     b = c
     print(c)

fibbinocci(2)