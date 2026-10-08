#496:Problem
class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        next_greater = {}
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)
        while stack:
            next_greater[stack.pop()] = -1
        return [next_greater[num] for num in nums1]
obj = Solution()
nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(obj.nextGreaterElement(nums1, nums2))