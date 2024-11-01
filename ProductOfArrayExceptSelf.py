# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 
# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 
# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


def productExceptSelf( nums):
    # Brute Force Approach
    zero_count = nums.count(0)
    product = 1
    if zero_count > 1:
        return [0]*len(nums)
    for num in nums:
        if num != 0:
            product *= num
    if zero_count == 0:
        return [product // x for x in nums]
    else:
        return [product if x == 0 else 0 for x in nums]
nums = [1,2,3,4]
print("Brute Force Approach",productExceptSelf(nums))

def productExceptSelf( nums):
    # Brute Force Approach
    n = len(nums)
    answer = [1] * n  
    prefix_product = 1
    for i in range(n):
        answer[i] = prefix_product
        prefix_product *= nums[i]
    suffix_product = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix_product
        suffix_product *= nums[i]
    return answer
nums = [-1,1,0,-3,3]
print("Optimal Approach",productExceptSelf(nums))