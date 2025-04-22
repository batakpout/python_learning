"""
Since the loop runs power times, the total time complexity is linear in the exponent, i.e., O(power)
"""


def iterative(base, power):
    result = 1
    while power >= 1:
        result *= base
        power -= 1
    return result


"""
Time-complexity:
The function makes power total recursive calls before reaching the base case (power == 0)
Each call performs:1 multiplication (base * ...), 1 subtraction (power - 1), One comparison (if power == 0).These are constant-time operations (O(1)) per call.
Since there are power recursive calls, the time complexity is O(power)
Space Complexity:
Due to recursion, the space complexity is O(power) because the call stack grows linearly with power.
Example: For power = 5, the call stack holds 5 frames before unwinding.
Comparison with Iterative Version:
The iterative version (iterative(base, power)) also has O(power) time complexity but O(1) space complexity (no call stack overhead).
"""


def recursiveInEfficient(base, power):
    if power == 0:
        return 1
    return base * recursiveInEfficient(base, power - 1)


if __name__ == "__main__":
    base = int(input("Enter base:"))
    power = int(input("Enter power:"))
    # result = iterative(base, power)
    result = recursiveInEfficient(base, power)  # lead to SOE for large inputs
    print(result)
