def printIncreasingDecreasing(n):
    if n == 0:
        return
    print(n)
    printIncreasingDecreasing(n - 1)
    print(n)

"""
Summary
Complexity	Recursive Version	
Time	        O(n)	            
Space	    O(n) (stack)	

"""

if __name__ == "__main__":
    printIncreasingDecreasing(5)
