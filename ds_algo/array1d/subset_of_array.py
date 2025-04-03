import math

def subSets(input_arr):
    n = len(input_arr)
    total_subsets = int(math.pow(2, n))
    for i in range(0, total_subsets):
        result = ""
        dec = i
        for j in range(n-1, -1, -1): # goes from 2 to 0 if n is 3
            rem = dec % 2
            if rem == 0:
                result = "_" + result
            else:
                result = input_arr[j] + result
            dec = dec // 2

        print(result)
    print()


if __name__ == "__main__":
    char_arr = "123" # or ['a', 'b', 'c']
    subSets(char_arr)