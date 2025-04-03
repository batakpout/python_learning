def min_max(nums):
    if not nums:
        raise ValueError("numay cannot be empty") #If a is an empty list ([]), not a evaluates to True

    min_val = nums[0]
    max_val = nums[0]

    for num in nums:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num

    return min_val, max_val


if __name__ == "__main__":
    print("Enter 5 array elements:")
    nums= [int(input()) for _ in range(5)]
    """nums= []  # Create an empty list
      for i in range(5):  # Loop 5 times, 0 to 4 inclusive
          num = int(input())  # Take user input and convert it to an integer
          num.append(num)  # Add the integer to the list"""

    result = min_max(nums)
    span = result[1] - result[0]

    # Output the span
    print("Span:", span)
