def f(base, power):
    if power == 0:
        return 1
    x = f(base, power // 2)
    x = x * x
    if power % 2 != 0:
        x = x * base
    return x


"""
Time-complexity:
The function uses divide-and-conquer (halving power in each recursive call).
The number of recursive calls is O(log₂(power)) because power is divided by 2 each time.
Each call performs:1 division(power // 2),1 or 2 mult (x*x and possibly x * base),1 modulo check (power % 2).
All operations per call are O(1), so total time is O(log power).

Space Complexity: O(log power)
The recursion depth is log₂(power) (each call halves power).
Each call adds a stack frame, so space is O(log power).

"""

if __name__ == "__main__":
    base = int(input("Enter base:"))
    power = int(input("Enter power:"))
    result = f(base, power)
    print(result)
