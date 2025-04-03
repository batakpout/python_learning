from typing import  Dict
def binary_search(arr, low, high, target):
    while low <= high:
        mid = low + (high - low) // 2 ## watch // here
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1

"""
 TC: sort-> O(n log n), binary search -> O(Log N), arr traverse -> O(n) 
  so, binary search + traverse -> O(N Log N)
  total: O(n log n) + O(N log N)
  AS: O(1)
"""
def using_binary_search(arr, target):
    arr.sort() #this does in-place sorting(Modifies the original list) doesn't return anything, sorted(arr)  # Returns a new sorted list
    n = len(arr)
    for i in range(n):
        complement = target - arr[i]
        result = binary_search(arr, i+1, n-1, complement)
        if result != -1:
            return i, result
    return -1, -1

"""
 TC: sort -> O(N Log N), no traverse complexity because we don't traverse whole array
 AS: O(1)
 This approach is the best approach for a sorted array. But if array is not sorted, then we use hashing.
"""
def using_two_pointers(arr, target):
    arr.sort()
    left, right = 0, len(arr) - 1
    while left < right:
        s = arr[left] + arr[right]
        if s == target:
            return left, right
        elif s > target:
             right -= 1
        else:
            left += 1
    return -1, -1

"""
TC: O(n²), for using two nested loops
AS: O(1)
"""
def two_sum_using_arrays(arr, target):
    n = len(arr)
    for i in range(n):
        for j in range(i+1,  n):
            if arr[i] + arr[j] == target:
                return i, j
    return -1, -1

"""
enumerate() is a Python function that adds a counter to any iterable (like a list) and returns it as an enumerate object containing (index, value) pairs.

  TC: O(n)
  Auxiliary space: O(n)
"""
def using_dict(arr, target) -> tuple[int, int]:
    dic: Dict[int, int] = {}
    for i, num in enumerate(arr):
        if num in dic:
            return dic[num], i
        dic[target-num] = i
    return -1, -1

"""
  TC: O(n)
  AS: O(n)
"""
def using_hashing(arr: list, target: int) -> bool:
    seen = set()
    for num in arr:
        if (target - num) in seen:
            return True
        seen.add(num)
    return False

def main():
    arr = [1, 3, 6, 7, 77, 9]
    target = 15
    result = using_dict(arr, target)

    if result[0] != -1:
        print(f"Pair found at indices {result[0]} and {result[1]}: {arr[result[0]]} + {arr[result[1]]} = {target}")
    else:
        print("No valid pair found")

if __name__ == "__main__":
    main()
