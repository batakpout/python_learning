
if __name__ == "__main__":
    """
     The number of contiguous(continuous) sub-arrays in an array of length  n = n⋅(n+1)/2
     TC: O(N * N *N), cubic complexity
     [1,2,3,4]
     sub-arrays: 1, 12, 123, 1234, 2, 23, 234, 3, 34, 4
     
     also this is a total string sub-strings  problem:
     A string of length n has n(n+1)/2 substrings.
     abc  [a, ab, abc, b, bc, c] contiguous
    """
def print_sub_arrays(nums):
    n = len(nums)
    for i in range(0, n):
        for j in range(i, n):
            for k in range(i, j+1):
                print(nums[k], end = " ")
            print()
        print()

nums = [10,20,30]
print_sub_arrays(nums)

def print_sub_string(char_arr):
    n = len(char_arr)
    for i in range(0, n):
        for j in range(i, n):
            for k in range(i, j+1):
                print(char_arr[k], end = " ")
            print()
        print()

print("-" * 10)
c_arr = ['a', 'b', 'c']
print_sub_string(c_arr)
