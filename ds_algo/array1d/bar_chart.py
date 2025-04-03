def maximum(nums) -> int:
    m = nums[0]
    for i in nums:
        if i > m:
            m = i
    return m

def bar_chart(nums):
    m = max(nums) # or just call maximum function
    while  m > 0:
        for item in nums:
            if item >= m:
                print("* ", end="")
            else:
                print("  ", end="")
        print()
        m-=1

def bar_chart2(nums, labels=None):
    max_val = max(nums)
    for level in range(max_val, 0, -1):  # Iterate from top to bottom
        #print('|'.join('*' if item >= level else ' ' for item in nums)) #generator expression
        print(' '.join('*' if item >= level else ' ' for item in nums)) #generator expression, here it gives back iterable to join method
    if labels:
        print(' '.join(labels))  # Print labels at the bottom


def bar_chart_fp(nums):
    max_level = max(nums)

    # Generate all levels from top to bottom
    levels = range(max_level, 0, -1)

    # For each level, create a row string
    def make_row(level):
        return ' '.join(map(lambda item: '*' if item >= level else ' ', nums))

    # Generate all rows and join with newlines
    return '\n'.join(map(make_row, levels))

def main():
    nums = [3,6,1,2,0,5]
    #bar_chart2(nums, labels=['A', 'B', 'C', 'D', 'E', 'F'])
    print(bar_chart_fp(nums))

if __name__ == "__main__":
    main()