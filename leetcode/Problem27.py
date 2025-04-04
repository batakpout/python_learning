"""
remove element
"""
from typing import List


def removeElement(nums: List[int], val: int) -> int:
     k = 0
     for i in range(len(nums)):
         if nums[i] != val:
             nums[k] = nums[i]
             k += 1
     return k

if __name__ == "__main__":
    print(removeElement([3,2,2,3], 3))
    print(removeElement([0,1,2,2,3,0,4,2], 2))