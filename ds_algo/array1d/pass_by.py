def mutate(arr):
    arr.append(4)

def reassign(arr):
    arr = [99, 100]

a = [1, 2, 3]
mutate(a)
print(a)  # [1, 2, 3, 4] ← mutated

reassign(a)
print(a)  # [1, 2, 3, 4] ← not changed

"""
Python uses "pass-by-object-reference" (also called "pass-by-assignment"):

When you pass a list (like arr: List[int]) to a function, you're passing a reference to the same object.

So, if you mutate the list (e.g., arr.append(5)), the original list is affected.

But if you reassign the parameter (e.g., arr = [1, 2, 3]), it only changes the local reference, not the original list.
"""