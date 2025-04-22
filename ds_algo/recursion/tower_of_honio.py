
def towerOfHonio(A, B, C, n):
    if n == 0:
        return
    else:
        towerOfHonio(A, C, B, n - 1)
        print(f"Moving disc {n} from {A} -> {B}")
        towerOfHonio(C, B, A, n - 1)

"""
# Time Complexity Analysis of Tower of Hanoi:
#
# The Tower of Hanoi problem has a recursive solution where:
#   T(n) = 2*T(n-1) + 1
# This results in a binary tree of height `n`, where each level doubles the number of calls.
#
# For n = 3, the recursion tree looks like:
#            n=3
#          /     \
#       n=2       n=2
#      /   \     /   \
#    n=1  n=1  n=1  n=1
#   ...  (continues until n=0) --> no of function calls
#
# Number of calls at each level:
#   Level 0: 1     → 2^0
#   Level 1: 2     → 2^1
#   Level 2: 4     → 2^2
#   Level 3: 8     → 2^3
#   Total calls: 1 + 2 + 4 + 8 = 15 = 2^(n+1) - 1
#
# Therefore, the time complexity is:
#   T(n) = O(2^n)

# Let’s calculate T(3):
# 
# T(3) = 2*T(2) + 1
# 
# T(2) = 2*T(1) + 1
# 
# T(1) = 2*T(0) + 1 = 1 (Base case: 1 move) → So:
# 
# T(2) = 2*1 + 1 = 3
# 
# T(3) = 2*3 + 1 = 7
# 
# ✅ It takes 7 steps to move 3 disks.
# Space complexity (due to recursion stack) is O(n)

"""
if __name__ == "__main__":
    towerOfHonio('A', 'B', 'C', 3)