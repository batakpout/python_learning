"""
Prints all unique pairs of elements in the nums.
Example: [1,2,3,4,5] → 1,2  1,3  1,4  1,5  2,3  2,4  2,5  3,4  3,5  4,5
"""

def print_pairs(nums):
    n = len(nums)
    for i in range(n):
        x = nums[i]
        for j in range(i + 1, n):
            y = nums[j]
            print(f"{x},{y}")
        print()


def main():
    nums= [1, 2, 3, 4, 5]
    print_pairs(nums)


if __name__ == "__main__":
    main()
