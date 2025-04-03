def multiply(arr1, arr2):
    if len(arr1[0]) != len(arr2):
        raise ValueError("Number of columns in 'arr1' must match rows in 'arr2'")

    arr3 = [[None for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            s = 0
            for k in range(len(arr2)):
                s += arr1[i][k] * arr2[k][j]
            arr3[i][j] = s
    return arr3


if __name__ == "__main__":
    arr_2d1 = []
    arr_2d2 = []
    rows1 = int(input("Enter number of rows for first array: "))
    cols1 = int(input("Enter number of columns for first array: "))

    print(f"Enter first {rows1}x{cols1} array:")
    for i in range(rows1):
        row = []
        for j in range(cols1):
            value = int(input(f"Enter value for [{i}][{j}]: "))
            row.append(value)
        arr_2d1.append(row)

    rows2 = int(input("Enter number of rows for second array: "))
    cols2 = int(input("Enter number of columns for second array: "))

    print(f"Enter second {rows2}x{cols2} array:")
    for i in range(rows2):
        row = []
        for j in range(cols2):
            value = int(input(f"Enter value for [{i}][{j}]: "))
            row.append(value)
        arr_2d2.append(row)

    print("\nEntered 2D array1:")
    for row in arr_2d1:
        print(row)

    print("\nEntered 2D array2:")
    for row in arr_2d2:
        print(row)

    print("Now multiplying them...")

    result = multiply(arr_2d1, arr_2d2)
    for row in result:
        print(row)
