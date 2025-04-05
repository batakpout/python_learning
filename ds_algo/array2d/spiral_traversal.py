def spiralTraversal(arr, row, col):
    if not arr:
        raise ValueError("Array must not be empty")

    total = row * col
    min_r, min_c, max_r, max_c = 0, 0, len(arr) - 1, len(arr[0]) - 1
    count = 0
    while count < total:
        i = min_r
        j = min_c
        while i <= max_r and count < total:
            print(arr[i][j])
            i += 1
            count += 1
        min_c += 1

        i = max_r
        j = min_c
        while j <= max_c and count < total:
            print(arr[i][j])
            j += 1
            count += 1
        max_r -= 1

        i = max_r
        j = max_c
        while i >= min_r and count < total:
            print(arr[i][j])
            i -= 1
            count += 1
        max_c -= 1

        i = min_r
        j = max_c
        while j >= min_c and count < total:
            print(arr[i][j])
            j -= 1
            count += 1
        min_r += 1




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

    print("printing spiral traversal: ")
    spiralTraversal(arr_2d, row, col)
