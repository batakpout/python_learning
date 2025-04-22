from typing import List

"""
    the 2d array is already sorted in both rows and columns
--> If the matrix is square or nearly square, stairCaseSearch is better (O(rows + cols)).
--> If the matrix has a very large number of columns compared to rows, searchMatrix (row-wise binary search)
    is better (O(rows × log cols)).
--> space complexity for both: O(1)
"""


def stairCaseSearch(matrix: List[List[int]], target: int) -> tuple[int, int]:
    row = len(matrix) - 1
    col = len(matrix[0]) - 1
    if target < matrix[0][0] or target > matrix[row][col]:
        return -1, -1

    i, j = 0, col
    while i <= row and j >= 0:
        if matrix[i][j] == target:
            return i, j
        elif target > matrix[i][j]:
            i += 1
        else:
            j -= 1
    return -1, -1


def binarySearch(i, low, high, target, matrix: List[List[int]]):
    while low <= high:
        mid = low + (high - low) // 2
        if matrix[i][mid] == target:
            return True
        elif matrix[i][mid] > target:
            high = mid - 1
        else:
            low = mid + 1


# try this
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    for i in range(len(matrix)):
        low = 0
        high = len(matrix[i]) - 1
        binarySearch(i, low, high, target, matrix)
    return False


if __name__ == "__main__":
    arr_2d = []

    row = int(input("Enter row size: "))
    col = int(input("Enter col size:"))

    print(f"Enter sorted {row}x{col} array")
    for i in range(row):
        r = []
        for j in range(col):
            value = int(input(f"enter element [{i}][{j}]: "))
            r.append(value)
        arr_2d.append(r)

    print("Entered array: ")
    for r in arr_2d:
        print(r)
    target = int(input("enter target to find: "))

    result: tuple[int, int] = stairCaseSearch(arr_2d, target)
    if result[0] == -1 and result[1] == -1:
        print("Element not found in the matrix")
    else:
        print(f"found at index, {result[0]}, {result[1]}")

    print("--" * 20)
    """
    [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    """
    binarySearchResult = searchMatrix(arr_2d, target)
    print(f"found: {binarySearchResult}")
