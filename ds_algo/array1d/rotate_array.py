def reverse(nums, left, right):
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

def rotate(nums, k):
    n = len(nums)
    k = k % n
    if k < 0:
        k = k + n
    print(f"k = {k}")
    reverse(nums, 0, n - k - 1)
    reverse(nums, n - k, n - 1)
    reverse(nums, 0, n - 1)




if __name__ == "__main__":
    print(f"Enter 7 array elements:")
    #nums = [int (input()) for _ in range(7)]
    nums  = [1,2,3,4,5,6,7]
    print("enter k:")
    k = int(input())
    rotate(nums, k)
    print(f"rotated array by {k}")
    print(",".join(map(str, nums)))
