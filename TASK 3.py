import math

n = int(input('Type in an integer: '))

def sqr(n):
    if int(math.sqrt(n) + 0.5) ** 2 == n:
        return True
    else:
        return False

print(math.sqrt(n),',', sqr(n))