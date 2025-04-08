from typing import List

"""
    length of 1D array calculation:
    leftSide            + lowerSide             + rightSide             + upperSide
    (max_r - min_r + 1) + (max_c - min_c + 1)   + (max_r - min_r + 1)   + (max_c - min_c + 1) -> 5 -1 = 4 + 1 = 5 items from 1 to 5
    ==> 2 * (max_r - min_r + 1) + 2 * (max_c - min_c + 1)
    ==> 2 * ((max_r - min_r) + (max_c - min_c))
"""


def reverse(arr_1d, left, right):
    while left < right:
        arr_1d[left], arr_1d[right] = arr_1d[right], arr_1d[left]
        left += 1
        right -= 1


def rotate(arr_1d, k):
    n = len(arr_1d)
    k = k % n
    if k < 0:
        k = k + n
    reverse(arr_1d, 0, n - k - 1)
    reverse(arr_1d, n - k, n - 1)
    reverse(arr_1d, 0, n - 1)
    return arr_1d


def make1DFromShell(arr_2d, s) -> List[int]:
    min_r = s - 1
    max_r = len(arr_2d) - 2
    min_c = s - 1
    max_c = len(arr_2d[0]) - 2
    size = 2 * ((max_r - min_r) + (max_c - min_c))
    arr_1d = [0] * size

    print(f"min_r: {min_r}")
    print(f"max_r: {max_r}")
    print(f"min_c: {min_c}")
    print(f"max_c: {max_c}")
    print(f"size: {size}")

    i, j, idx = min_r, min_c, 0
    while i <= max_r:
        arr_1d[idx] = arr_2d[i][j]
        i += 1
        idx += 1
    min_c += 1

    i, j = max_r, min_c
    while j <= max_c:
        arr_1d[idx] = arr_2d[i][j]
        j += 1
        idx += 1
    max_r -= 1

    i, j = max_r, max_c
    while i >= min_r:
        arr_1d[idx] = arr_2d[i][j]
        i -= 1
        idx += 1
    max_c -= 1

    i, j = min_r, max_c
    while j >= min_c:
        arr_1d[idx] = arr_2d[i][j]
        j -= 1
        idx += 1

    return arr_1d


def makeShellFrom1D(arr_2d, arr_1d, s) -> List[int]:
    min_r = s - 1
    max_r = len(arr_2d) - 2
    min_c = s - 1
    max_c = len(arr_2d[0]) - 2

    i, j, idx = min_r, min_c, 0
    while i <= max_r:
        arr_2d[i][j] = arr_1d[idx]
        i += 1
        idx += 1
    min_c += 1

    i, j = max_r, min_c
    while j <= max_c:
        arr_2d[i][j] = arr_1d[idx]
        j += 1
        idx += 1
    max_r -= 1

    i, j = max_r, max_c
    while i >= min_r:
        arr_2d[i][j] = arr_1d[idx]
        i -= 1
        idx += 1
    max_c -= 1

    i, j = min_r, max_c
    while j >= min_c:
        arr_2d[i][j] = arr_1d[idx]
        j -= 1
        idx += 1

    return arr_2d


def shellRotate(arr_2d, s, k):
    arr_1d = make1DFromShell(arr_2d, s)
    print("1d array formed")
    print(arr_1d)
    arr_1d = rotate(arr_1d, k)
    print("rotated array by 2")
    print(arr_1d)
    arr_2d_new = makeShellFrom1D(arr_2d, arr_1d, s)
    return arr_2d_new


if __name__ == "__main__":
    arr_2d = []

    row = int(input("Enter row size: "))
    col = int(input("Enter col size:"))

    print(f"Enter {row}x{col} array")
    for i in range(row):
        r = []
        for j in range(col):
            value = int(input(f"enter element [{i}][{j}]: "))
            r.append(value)
        arr_2d.append(r)

    print("Entered array: ")
    for r in arr_2d:
        print(r)

    s = int(input("Enter the shell number to rotate:"))
    k = int(input("Enter number to rotate it by: "))

    print("printing shell rotated array: ")
    result = shellRotate(arr_2d, s, k)
    for r in result:
        print(r)
