def diffTwoLists(nums1, nums2):
    """
    keep 1000 - 1 or 1000 - 999 in mind leading zeros in result
    """
    n1 = len(nums1)
    n2 = len(nums2)
    #assume n2 has bigger number, and also its size is larger
    c, i, j, k = 0, n1 - 1, n2 - 1, n2 - 1
    diff = [None] * n2 #a list of size n2 with all elements initialized to None
    # here j refers to n2 i.e largest array, i to n1 i.e smallest array and k to diff array
    while k >= 0:
        n1_list_value = nums1[i] if i>=0 else 0
        d = 0
        if c + nums2[j] >= n1_list_value:
            d = c + nums2[j] - n1_list_value
            c = 0
        else:
            d = c + 10 + nums2[j] - n1_list_value
            c = -1

        diff[k] = d
        i -= 1
        j -= 1
        k -= 1

    idx = 0
    while idx <= n2:
        if diff[idx] == 0:
            idx += 1
        else:
            break

    for i in range(idx, n2):
        print(diff[i], end = " ")


if __name__ == "__main__":
    print("enter largest list:")
    a1 = list(map(int, input().split())) # same as a1 = [int(x) for x in input().split()]
    print("enter smaller list:")
    a2 = list(map(int, input().split()))
    diffTwoLists(a2, a1) # a2 > a1