#1248 problem: Count Number of Nice Subarrays
'''from typing import List
def numberOfSubarrays(self, nums: List[int], k: int) -> int:
    def atmost(goal: int) -> int:
        if goal<0:
            return 0 
        left = 0
        count=0
        odd_count=0
        for right in range(len(nums)):
            if nums[right]%2 !=0:
                odd_count+=1
            while odd_count>goal:
                if nums[left]%2!=0:
                    odd_count-=1
                left+=1
            count+=right-left+1
        return count
    return atmost(k)-atmost(k-1)
nums = [1,1,2,1,1]
k = 3
print(numberOfSubarrays(None, nums, k))'''
#1763 problem: Longest Nice Subarray
from typing import List
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s)<2:
            return ""
        char_set = set(s)
        for i,char in enumerate(s):
            if char.swapcase() not in char_set:
                s1 = self.longestNiceSubstring(s[:i])
                s2 = self.longestNiceSubstring(s[i+1:])
                return s1 if len(s1)>=len(s2) else s2
        return s
nums = "YazaAay"
print(Solution().longestNiceSubstring(nums))