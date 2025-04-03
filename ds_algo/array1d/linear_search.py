def linearSearch(nums, key):
    for i in range(len(nums)):
        if nums[i] == key:
            return i
    return -1

def main():
    nums= [10,20,30,40.50]
    key = 20
    result = linearSearch(nums, key)
    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found in the numsay.")