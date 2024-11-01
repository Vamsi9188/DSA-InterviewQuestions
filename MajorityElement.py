# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 
# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
 

# Constraints:

# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109


def majorityElement(nums):
# Brute Force Approach
    counts = {}
    for num in nums:
        # counts[num]=counts.get(num,0)+1
        if num in counts:
            counts[num]+=1
        else:
            counts[num]=1
        if counts[num]>len(nums)//2:
            return num
nums = [2,2,1,1,1,2,2]
print("Brute Force Approach:",majorityElement(nums))

# Optimized Approach
def majorityElement(nums):
    majorityElement=None
    count=0
    for num in nums:
        if count==0:
            majorityElement=num
        count += (1 if majorityElement==num else -1)
    return majorityElement
nums = [3,2,3]        
print("Optimal Approach:",majorityElement(nums))