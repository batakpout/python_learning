def firstOcc(arr, l, idx, target):
    if idx == l:
        return -1
    res = firstOcc(arr, l, idx + 1, target)
    if arr[idx] == target:
        return idx
    else:
        return res


"""
Time Complexity: O(n) (each element checked once).

Space Complexity: O(n) (only due to recursion stack, no slicing).
"""


def lastOcc(arr, l, idx, target):
    if idx == l:
        return -1
    res = lastOcc(arr, l, idx + 1, target)  # slice arr[1:] = arr + 1 in c++
    if res == -1:
        if arr[idx] == target:
            return idx
        else:
            return -1
    else:
        return res

"""
Time Complexity: O(n)

Space Complexity: O(n)
"""


def AllOcc(arr, l, idx, target, fsf):  # fsf --> found so far
    if idx == l:
        return [0] * fsf

    if arr[idx] == target:
        res = AllOcc(arr, l, idx + 1, target, fsf + 1)
        res[fsf] = idx  # can't use .append as it return None
        return res
    else:
        return AllOcc(arr, l, idx + 1, target, fsf)

"""
Time Complexity: O(n)

Space Complexity: O(n + k)
n = length of input array (recursion stack depth)
k = number of matches found (size of result list)

"""
if __name__ == "__main__":
    print("enter array of 10 elements")
    a = [int(input()) for _ in range(10)]
    target = int(input("enter target:"))
    r1 = firstOcc(a, len(a), 0, target)
    print(f"{target} first occurs at index: {r1}")
    r2 = lastOcc(a, len(a), 0, target)
    print(f"{target} last occurs at index: {r2}")
    r3 = AllOcc(a, len(a), 0, target, 0)
    print(f"all occurances of {target}: {r3}")
