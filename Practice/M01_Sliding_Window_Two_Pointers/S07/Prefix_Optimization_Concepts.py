'''1480.Problem: Running Sum of 1d Array
arr = list(map(int, input("Enter elements: ").split()))
running_sum = 0
result = []
for num in arr:
    running_sum += num
    result.append(running_sum)
print("Running sum:", result)

1732. Find the Highest Altitude
#optimal solution
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = 0
        highest = 0
        for g in gain:
            alt+=g
            highest = max(highest, alt)
        return highest
method_2
n = len(gain)
alt = [0]*(n+1)
for i in range(1,n+1):
    alt[i] = alt[i-1]+gain[i-1]
return max(alt)

1991. Find the Middle Index in Array
class Solution:
    def findMiddleIndex(self, nums):
        totalSum = sum(nums)
        leftSum = 0

        for i in range(len(nums)):
            rightSum = totalSum - leftSum - nums[i]

            if leftSum == rightSum:
                return i

            leftSum += nums[i]

        return -1



724. Find Pivot Index

'''