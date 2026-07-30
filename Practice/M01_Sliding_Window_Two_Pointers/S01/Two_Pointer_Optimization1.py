#Remove Duplicates from Sorted Array
'''from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
        return j + 1
nums = [0,0,1,1,1,2,2,3,3,4]
sol = Solution()
k = sol.removeDuplicates(nums)
print("k =", k)
print("First k elements:", nums[:k])
print("Entire array:", nums)'''

from typing import List
def removeElement(nums: List[int], val: int) -> int:
    i=0
    for j in range(len(nums)):
        if nums[j]!=val:
            nums[i]=nums[j]
            i+=1
    return i
nums = [3,2,2,3]
val = 3
print(removeElement(nums,val))