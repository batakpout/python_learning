## square matrix
def rotate(arr):
    ##transpose first
    for i in range(len(arr)):
        for j in range(i + 1, len(arr[0])):
            arr[j][i], arr[i][j] = arr[i][j], arr[j][i]

    for r in arr:
        print(r)
    print("========")
    ## reverse each 1d array
    for i in range(len(arr)):
        left, right = 0, len(arr[i]) - 1
        while left < right:
            arr[i][left], arr[i][right] = arr[i][right], arr[i][left]
            left += 1
            right -= 1

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