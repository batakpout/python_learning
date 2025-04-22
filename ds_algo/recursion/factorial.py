def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


"""
Each call performs:A constant-time multiplication (n * ...), A constant-time subtraction (n - 1),A comparison (if n == 1).
Since the work per call is O(1), and there are n calls, the total time complexity is O(n).

Each recursive call adds a new stack frame, consuming memory.
The maximum depth of the call stack is n (e.g., factorial(5) uses 5 stack frames).
Hence, space complexity is O(n) (due to recursion).

"""
if __name__ == "__main__":
    print(factorial(6))
