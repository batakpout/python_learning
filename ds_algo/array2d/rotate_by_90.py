## square matrix
def rotate(arr):
    ##transpose first
    for i in range(len(arr)):
        for j in range(i + 1, len(arr[0])):
            arr[j][i], arr[i][j] = arr[i][j], arr[j][i]  # todo check how this swap works

    ## now reverse each row in the matrix after transpose
    for i in range(len(arr)):
        left, right = 0, len(arr[i]) - 1
        while left < right:
            arr[i][left], arr[i][right] = arr[i][right], arr[i][left]
            left += 1
            right -= 1

"""
Final Time Complexity:
Transpose: O(n²), because j runs from i + 1 and does n-1 swaps in first iteration, n-2 in second, 1 in last, 0
so, n-1 + n-2 + .. + 1 ==> n * n
if this 2d array was not square then, O(n * m)

Reverse Rows: O(n²) 

Total: O(n²) + O(n²) = O(n²)
Space Complexity: O(1)
"""
if __name__ == "__main__":
    arr_2d = []

    row = int(input("Enter row size: "))
    col = int(input("Enter col size:"))

    print(f"Enter {row}x{col} square array")
    for i in range(row):
        r = []
        for j in range(col):
            value = int(input(f"enter element [{i}][{j}]: "))
            r.append(value)
        arr_2d.append(r)

    print("Entered array: ")
    for r in arr_2d:
        print(r)

    print("printing rotated by 90 array: ")
    rotate(arr_2d)
    for r in arr_2d:
        print(r)
