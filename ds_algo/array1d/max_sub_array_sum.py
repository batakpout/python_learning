# this has cubic complexity O(n * n * n)
def usingBruteForce(nums):
    largest_sub_array_sum = 0
    n = len(nums)
    for i in range(0, n):
        for j in range(i, n):
            sub_array_sum = 0
            for k in range(i, j + 1):
                sub_array_sum += nums[k]
            largest_sub_array_sum = max(largest_sub_array_sum, sub_array_sum)

    return largest_sub_array_sum


# complexity O(n * n)
def usingPrefixSum(nums):
    n = len(nums)
    largest_sub_array_sum = 0

    for i in range(1, n):
        nums[i] += nums[i - 1]  # builds prefix sum array

    for i in range(n):
        for j in range(i, n):
            sub_array_sum = nums[j] if i == 0 else nums[j] - nums[i - 1]  # conditional expression (ternary operator)
            largest_sub_array_sum = max(largest_sub_array_sum, sub_array_sum)

    return largest_sub_array_sum


# complexity O(N) linear time complexity, assumes at least one positive item in the list
def kadanes_method(nums):
    cs = 0
    max_sum = 0
    for item in nums:
        cs += item
        if cs < 0:
            cs = 0
        max_sum = max(max_sum, cs)
    return max_sum


if __name__ == "__main__":
    nums = [-2, 3, 4, -1, 5, -12, 6, 1, 3, 2]
    # result = usingBruteForce(nums)
    # result = usingPrefixSum(nums)
    result = kadanes_method(nums)
    print(result)
# some say: When all elements are negative, the maximum subarray is the empty subarray, which has sum 0.
"""
Works for positive and negative both, kaden's

int modifiedkadane(int *a,int n){
    int sum = INT_MIN; // largest sum
    int currsum = 0;   // current running sum
    int maxelem = INT_MIN; // to find max ele (needed for all negative case ones)
   
    for(int i=0;i<n;i++){
        currsum += a[i];
        if(currsum < 0){
            currsum = 0;
        }
        sum = max(sum,currsum); // till here code is same as kadane algo code
        if(maxelem < a[i]){     // to calculate max ele (needed for all -ve case)
            maxelem = a[i];
        }
    }
    return (maxelem < 0 ? maxelem : sum);//if all are -ve return maxelem, else sum
}
"""
