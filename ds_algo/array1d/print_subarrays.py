
if __name__ == "__main__":
    """
     The number of contiguous sub-arrays in an array of length  n = n⋅(n+1)/2
     TC: O(N * N *N), cubic complexity
     [1,2,3,4]
     sub-arrays: 1, 12, 123, 1234, 2, 23, 234, 3, 34, 4
    """
def print_sub_arrays(nums):
    n = len(nums)
    for i in range(0, n):
        for j in range(i, n):
            for k in range(i, j+1):
                print(nums[k], end = " ")
            print()
        print()

nums = [10,20,30,40,50, 60]
print_sub_arrays(nums)
