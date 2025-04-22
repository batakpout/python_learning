

def fibo(n):
    if n == 0 or n == 1:
        return n
    return fibo(n - 1) + fibo(n - 2)

def print_fibo_series(n):
    for i in range(n + 1):
        print(fibo(i))

"""
Time-complexity:
Recursive Fibonacci with O(2^n) time complexity.
    Total function calls grow exponentially:
    - 1 call for fib(n)
    - 2 calls for fib(n-1)+fib(n-2)
    - 4 calls at next level
    - Forms a geometric progression (GP) ~ 2^n total calls
"""

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    #print(fibo(n))
    print_fibo_series(n)