import math

"""
 Sieve of Eratosthenes algorithm
 Time Complexity: O(n log log n) where n is the upper_bound
 We need to create a boolean array of size upper_bound, which is approximately n log n, So the space complexity is O(n log n)
 how to find the upper_bound
 Using the Prime Number Theorem: The nth prime number Pₙ is approximately n × ln(n). 
 For n=10000, this gives us ~92100. Adding a safety margin (like multiplying by 1.2) gives us ~110520, which is close to the 110000 we used
"""
def find_nth_prime(n):
    """
    n = 10000 , maximum value
     the 10000th prime is 104729, which is far larger than 10001. If we only sieved up to 10001, we would only find approximately 1200 primes, not 10000.
    """
    upper_bound = 110000

    # Create the sieve
    is_prime = [True] * (upper_bound + 1)
    is_prime[0] = is_prime[1] = False

    # Fill the sieve
    for i in range(2, math.isqrt(upper_bound) + 1):
        if is_prime[i]:
            for j in range(i * i, upper_bound + 1, i):
                is_prime[j] = False

    # Count primes until we reach the nth one
    count = 0
    for i in range(2, upper_bound + 1):
        if is_prime[i]:
            count += 1
            if count == n:
                return i

    # If we get here, our upper bound wasn't high enough
    return "Upper bound too small for this value of n"


if __name__ == "__main__":
    n = int(input("enter n: "))
    prime = find_nth_prime(n)
    print(f"The {n}th prime number is: {prime}")