import math

"""
      TC: square_root(n), no of iterations is roughly square_root(n) / 2 [worst case]
      SC:  O(1) (constant space)
"""


def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    max_divisor = math.isqrt(n) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False

    return True


if __name__ == "__main__":
    print(isPrime(2))
    print(isPrime(-101))
    print(isPrime(37))
    print(isPrime(96))
    print(isPrime(13))
    print(isPrime(39))
