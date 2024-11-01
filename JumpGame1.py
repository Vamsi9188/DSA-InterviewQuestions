# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

 

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

# Constraints:

# 1 <= nums.length <= 104
# 0 <= nums[i] <= 105

# Optimized Approach (Greedy)
def canJump(nums):
    last_pos = len(nums) - 1
    for i in range(len(nums) - 1, -1, -1):
        if i + nums[i] >= last_pos:
            last_pos = i
    return last_pos == 0
nums = [2,3,1,1,4]
print("Optimal Approach",canJump(nums))

# Brute Force Approach (DFS)
def canJump(nums):
    n = len(nums)
    reachable = [False] * n
    reachable[0] = True
    for i in range(n):
        if reachable[i]:
            for j in range(i + 1, min(i + nums[i] + 1, n)):
                reachable[j] = True
            if reachable[-1]:  
                return True
    return reachable[-1]
nums = [3,2,1,0,4]
print("Brute Force Approach",canJump(nums))