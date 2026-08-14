#209.Problem: Minimum Size Subarray Sum
'''from typing import List
def minSubArrayLen( target: int, nums: List[int]) -> int:
    left = 0
    curr_sum = 0
    min_len = float('inf')
    for right in range(len(nums)):
        curr_sum += nums[right]
        while curr_sum>=target:
            min_len = min(min_len,right-left+1)
            curr_sum -= nums[left]
            left+=1
    return min_len if min_len!=float('inf') else 0 
target = 7
nums = [2,3,1,2,4,3]
print(minSubArrayLen(target,nums))'''
#713.Problem: Subarray Product Less Than K
from typing import List
def numSubarrayProductLessThanK(nums: List[int], k: int) -> int:
    if k<=1:
        return 0
    left = 0
    pro = 1
    c = 0
    for right in range(len(nums)):
        pro *=nums[right]
        while pro>=k:
            pro//=nums[left]
            left+=1
        c+=right-left+1
    return c
nums = [10,5,2,6]
k = 100
print(numSubarrayProductLessThanK(nums,k))