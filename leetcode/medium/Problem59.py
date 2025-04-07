from typing import List


def spiral_traversal2(n:int) -> List[List[int]]:
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    min_r, min_c, max_r, max_c = 0, 0, n - 1, n - 1
    count = 1
    total = n * n

    while count <= total:
        i = min_r
        j = min_c
        while j <= max_c and count <= total:
            matrix[i][j] = count
            j += 1
            count += 1
        min_r += 1

        i = min_r
        j = max_c
        while i <= max_r and count <= total:
            matrix[i][j] = count
            i += 1
            count += 1
        max_c -= 1

        i = max_r
        j = max_c
        while j >= min_c and count <= total:
            matrix[i][j] = count
            j -= 1
            count += 1
        max_r -= 1

        i = max_r
        j = min_c
        while i >= min_r and count <= total:
            matrix[i][j] = count
            i -= 1
            count += 1
        min_c += 1
    return matrix


if __name__ == "__main__":
    arr_2d = []

    n = int(input("Enter n: "))


    print(f"generating spiral array of size: {n *n} ")
    result = spiral_traversal2(n)

    for r in result:
        print(r)
