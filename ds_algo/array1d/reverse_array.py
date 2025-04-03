def reverse(nums):
    left, right = 0, len(nums) - 1 #tuple unpacking, meaning both left and right are assigned simultaneously and in parallel
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

def main():
    nums= []
    print("Enter array of size 5: ")
    for _ in range(5):
        nums.append(int(input()))

    print("Entered array:")
    print(",".join(map(str, nums)))

    reverse(nums)

    print("Entered array:")
    print(",".join(map(str, nums)))

if __name__ == "__main__":
    main()