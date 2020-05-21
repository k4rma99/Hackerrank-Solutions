from math import sqrt

def checkPrime(n):
    if n == 2:
        return ("Prime")
    if n % 2 == 0 or n == 1:
        return ("Not prime")
    sqr = int(sqrt(n))
    for i in range(3,sqr+1,2):
        if n % i == 0:
            return ("Not prime")
    return ("Prime")
    pass

t = int(input())
for i in range(t):
    n = int(input())
    print(checkPrime(n))