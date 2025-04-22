def display(arr, idx, l):
    if idx == l:
        return
    print(arr[idx])
    display(arr, idx + 1, l)

def reverseDisplay(arr, idx, l):
    if idx == l:
        return
    reverseDisplay(arr, idx + 1, l)
    print(arr[idx])
"""
Function	        Order of Printing	            Time Complexity	    Space Complexity
display	Forward     (arr[0] to arr[n-1])	        O(n)	            O(n) (recursion stack)
reverseDisplay	    Backward (arr[n-1] to arr[0])	O(n)	            O(n) (recursion stack)
"""

if __name__ == "__main__":
    print("enter 5 array elements:")
    a = [int(input()) for _ in range(5)]
    print("displaying arr:")
    display(a, 0, len(a))
    print("Now displaying in reverse:")
    reverseDisplay(a, 0, len(a))
