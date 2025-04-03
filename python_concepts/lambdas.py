"""
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.
Syntax:
lambda arguments : expression
The expression is executed and the result is returned
"""
if __name__ == "__main__":
    x = lambda a: a + 10
    print(x(10))
    y = lambda a, b: a + b
    print(y(10, 20))

def myFunc(n):
    return lambda a: a * n
myDoubler = myFunc(2)
print(myDoubler(3))


numbers = [2,3,4,5,6,7,8,9]
nums = list(range(1, 6))
total = sum(nums)
print(total)

def old_school(nums):
    t = 0
    for item in nums:
        if item % 3 == 0 or item % 5 == 0:
            t +=item
    return t

res0 = sum(x for x in numbers if x % 3 == 0 or x % 5 == 0)#generator expression.The generator lazily produces values one by one, instead of storing them all in memory.
res1 = sum(filter(lambda n: n % 3 == 0 or n % 5 == 0, numbers))

print(old_school(numbers))
print(res0)
print(res1)
print("======")

lambda_test = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"
"""
    same as 
    def n(x):
    if x > 0:
        return "Positive"
    elif x < 0:
        return "Negative"
    else:
        return "Zero"
  """
print(lambda_test(5))
print(lambda_test(-5))
print(lambda_test(0))
