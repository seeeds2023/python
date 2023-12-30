
def is_prime(num):    
    lim = int(num/2) + 1
    for i in range(2,lim):
        rem = num%i
        if rem == 0 :
            result = False
            break
        else:
            result = True

    return result

num = 8
result = is_prime(num)
print(f'is {num} prime? {result}')

    