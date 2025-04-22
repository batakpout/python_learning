def saddlePoint(arr):
    for i in range(len(arr)):
        lv = 0
        for j in range(1, len(arr[0])):
            if arr[i][j] < arr[i][lv]:
                lv = j
        saddle = True
        for k in range(len(arr)):
            if arr[k][lv] > arr[i][lv]:
                saddle = False
                break

        if saddle:
            print(f"saddle-point: {arr[i][lv]}")
            return

    print("invalid input, no saddle point found")

"""
n: rows
m: cols
So for each row, I do: O(m) work to find the row min, O(n) work to check column max
Total time per row = O(m + n)
Total for all rows = O(n * (m + n))

Final Time Complexity: O(mn + n*n)


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

    saddlePoint(arr_2d)
