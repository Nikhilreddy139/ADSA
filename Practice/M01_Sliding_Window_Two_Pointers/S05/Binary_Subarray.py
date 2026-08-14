#1493 Problem: Longest Subarray of 1's After Deleting One Element
'''from typing import List
def longestSubarray(self, nums: List[int]) -> int:
    left = 0
    zero_count = 0
    max_len = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1
        while zero_count > 1:
            if nums[left] == 0:
                zero_count -= 1
            left += 1
        max_len = max(max_len, right - left)
    return max_len
nums = [1,1,0,1]
print(longestSubarray(None, nums))

#1004 Problem: Max Consecutive Ones III
from typing import List 
def longestOnes(self, nums: List[int], k: int) -> int:
    left = 0
    max_len = 0c
    for right in range(len(nums)):
        if nums[right] == 0:
            k -= 1
        while k < 0:
            if nums[left] == 0:
                k += 1
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len
nums = [1,1,0,0,1,1,1,0,1,1]
k = 2
print(longestOnes(None, nums, k))'''
#930 problem: Binary Subarrays With Sum
from typing import List
def numSubarraysWithSum(nums: List[int], goal: int) -> int:
    count = {0: 1}
    curr_sum = 0
    result = 0
    for num in nums:
        curr_sum += num
        if curr_sum - goal in count:
            result += count[curr_sum - goal]
        count[curr_sum] = count.get(curr_sum, 0) + 1
    return result
nums = [1,0,1,0,1]
goal = 2
print(numSubarraysWithSum(nums, goal))