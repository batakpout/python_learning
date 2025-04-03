def increment_2d_array(arr):
    """Increment each element in a 2D array by 2"""
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j] += 2
    return arr


def main():
    # Get dimensions from user
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    # Initialize empty 2D array
    array_2d = []

    # Fill the 2D array with user input
    print(f"Enter {rows}x{cols} integers:")
    for i in range(rows):
        row = []
        for j in range(cols):
            value = int(input(f"Enter value for [{i}][{j}]: "))
            row.append(value)
        array_2d.append(row)

    # Print original array
    print("\nOriginal 2D array:")
    for row in array_2d:
        print(row)

    # Increment and get new array
    incremented_array = increment_2d_array(array_2d)

    # Print modified array
    print("\n2D array after incrementing each element by 2:")
    for row in incremented_array:
        print(row)


if __name__ == "__main__":
    main()