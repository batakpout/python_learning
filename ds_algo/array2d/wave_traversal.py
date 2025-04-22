def spiral_print(arr):
    for j in range(len(arr[0])):
            if j % 2 == 0:
                for i in range(len(arr)):
                    print(arr[i][j])
            else:
                for i in range(len(arr) - 1, -1 , -1):
                    print(arr[i][j])

"""
Time Complexity: O(m * n), where m is the number of rows and n is the number of columns in the input matrix.

Space Complexity: O(1) (constant space, no additional storage proportional to input size).
"""

if __name__ == "__main__":
    arr_2d = []

    row = int(input("Enter row size: "))
    col = int(input("Enter col size:"))

    print(f"Enter {row}x{col} array")
    for i in range(row):
        row = []
        for j in range(col):
            value = int(input(f"enter element [{i}][{j}]: "))
            row.append(value)
        arr_2d.append(row)

    print("Entered array: ")
    for row in arr_2d:
        print(row)

    print("printing spiral display: ")
    spiral_print(arr_2d)