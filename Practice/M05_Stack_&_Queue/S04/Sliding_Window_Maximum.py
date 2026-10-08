#239.Problem
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        res = []
        for i in range(len(nums) - k + 1):
            window = nums[i:i + k]
            res.append(max(window))
        return res
obj = Solution()
k=3
nums = [1,3,-1,-3,5,3,6,7]
print(obj.maxSlidingWindow(nums, k))