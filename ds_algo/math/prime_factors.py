import math


#TC: square_root(n)
def primeFactor(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i

    # If n is a prime number greater than 2
    if n > 2:
        factors.append(n)
    return factors

def maxPrimeFactor(n):
    max_prime = -1
    while n % 2 == 0:
        max_prime = 2
        n = n // 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            max_prime = i
            n //= i

    # If n is a prime number greater than 2
    if n > 2:
        max_prime = n
    return max_prime


if __name__ == "__main__":
    print(maxPrimeFactor(10))
    print(maxPrimeFactor(17))
