def exitPoint(arr):
    i, j, direction = 0, 0, 0

    while True:
        direction = (arr[i][j] + direction) % 4
        if direction == 0:
            j += 1
        elif direction == 1:
            i += 1
        elif direction == 2:
            j -= 1
        elif direction == 3:
            i -= 1

        print(f"i = {i}")
        print(f"j = {j}")

        if i < 0:
            i += 1
            break
        elif j < 0:
            j += 1
            break
        elif i >= len(arr):
            i -= 1
            break
        elif j == len(arr[0]):
            j -= 1
            break
    print("Exit point:", i, j)


"""

Complexity	Value	    Explanation
Time	    O(n × m)	In the worst case, every cell is visited once.
Space	    O(1)	    Only a few variables are used; no extra storage.

"""
if __name__ == "__main__":
    arr_2d = []

    row = int(input("Enter row size: "))
    col = int(input("Enter col size:"))

    print(f"Enter {row}x{col} array of 1's and 0's")
    for i in range(row):
        r = []
        for j in range(col):
            value = int(input(f"enter element [{i}][{j}]: "))
            r.append(value)
        arr_2d.append(r)

    print("Entered array: ")
    for r in arr_2d:
        print(r)

    print("printing exit point of a 2d array: ")
    exitPoint(arr_2d)
