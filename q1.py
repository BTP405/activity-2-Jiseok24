# Helper function - determine particular number is prime
def prime(num):
    if num < 2:
        return False
    for i in range (2, int(num**0.5) +1):
        if num % i == 0:
            return False
    return True

# getPrimeNumber funciton
def getPrimeNumber(n):
    return [x for x in range (2, n + 1) if prime(x)]


print(getPrimeNumber(20))
