def sumTwoLists(nums1, nums2):
    n1 = len(nums1)
    n2 = len(nums2)
    max_len = max(n1, n2)
    nums3 = [0] * max_len # create list of size max_len and [0] initializes with default value 0
    c, i, j, k = 0, n1 - 1, n2 - 1, max_len - 1
    while k >= 0:
        d = c
        if i >=0:
            d += nums1[i]

        if j >= 0:
            d += nums2[i]

        c = d // 10
        d = d % 10

        nums3[k] = d
        i -= 1
        j -= 1
        k -= 1

    if c > 0:
        print(c, end=" ")

    for i in range(0, len(nums3)):
        print(nums3[i], end = " ")


if __name__ == "__main__":
    print("enter first list:")
    a1 = list(map(int, input().split())) # same as a1 = [int(x) for x in input().split()]
    print("enter second list:")
    a2 = list(map(int, input().split()))
    sumTwoLists(a1, a2)