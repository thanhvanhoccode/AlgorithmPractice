#https://codelearn.io/learning/thuat-toan-can-ban
def isPrime(n):
    import math
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True
