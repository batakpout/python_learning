def diagonalTraversal(arr):
    for i in range(len(arr)):
        j = i
        k = 0
        while j < len(arr[0]):
            print(arr[k][j])
            k += 1
            j += 1

"""
Time Complexity: O(n * m), where n is the number of rows and m is the number of columns.

Space Complexity: The method uses a constant amount of extra space (variables i, j, k), regardless of the input size.

The input array is not counted toward space complexity since it’s part of the input.

Thus, the space complexity is O(1) (constant space).
"""
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

    print("printing upper diagonal traversal: ")
    diagonalTraversal(arr_2d)
