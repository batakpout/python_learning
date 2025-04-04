from typing import List


def removeDuplicates(nums: List[int]) -> int:
    if  not nums:
        return 0
    index_i = 0
    for index_j in range(1, len(nums)):
        if nums[index_i] != nums[index_j]:
            index_i += 1
            nums[index_i] = nums[index_j]
    return index_i + 1


if __name__ == "__main__":
    arr = []
    size = int(input("enter array size:"))
    for i in range(size):
        value = int(input(f"enter {i} element:"))
        arr.append(value)

    res = removeDuplicates(arr)
    print(res)
    print(arr)
