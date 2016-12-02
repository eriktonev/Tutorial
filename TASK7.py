n = int(input('Input a number, please: '))#ask user for input

def is_prime(n, a=3):

    if n == 2:#if n is 2 then its a prime
        prime = True
    elif n <= 1 or n % 2 == 0:#if its too small or round its not a prime
        prime = False
    elif a * a > n:#tried all divisors to sqrt so must be a prime
        prime = True
    elif (n % a) == 0:#if it divides evenly its not  prime
        prime = False
    else:#can't tell ? try again recursively with a new divisor
        prime = is_prime(n, a + 2)

    return prime#return result

print(is_prime(n, a=3))#print out result