# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
 

# Constraints:

# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1
# 0 <= k <= 105

def rotateArray(nums,k):
# Brute Force Approach (Efficient method)
    n = len(nums)
    k = k % n
    for ele in range(k):
        lastElement=nums.pop()
        nums.insert(0,lastElement)
    return nums
nums = [1,2,3,4,5,6,7]
k = 3
print("Brute Force:",rotateArray(nums,k))
    # for ele in range(k):
    #     lastElement=nums[n-1]
    #     for i in range(n-1,0,-1):
    #         nums[i]=nums[i-1]
    #     nums[0]=lastElement
    # return nums


# Optimized Approach
def rotateArray(nums,k):
    def reverse(nums,start,end):
        while start<end:
            nums[start],nums[end]=nums[end],nums[start]
            start += 1
            end -= 1
    n=len(nums)
    k=k%n
    reverse(nums,0,n-1)
    reverse(nums,0,k-1)
    reverse(nums,k,n-1)
    return nums
nums = [-1,-100,3,99]
k = 2
print("Optimal Approach:",rotateArray(nums,k))