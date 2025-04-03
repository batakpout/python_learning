def inverseOfArray(nums):
    max_val = max(nums) if nums else -1
    arr2 = [0] * len(nums)  # Ensure arr2 is large enough
    for i in range(0, len(nums)):
        arr2[nums[i]] = i
    return arr2

if __name__ == "__main__":
    nums = [3,4,1,2,0]
    res = inverseOfArray(nums)
    print(res)

    """
    index:  0 1 2 3 4 
    values: 3 4 1 2 0  [input]
    values: 4 2 3 0 1  [output]
    """