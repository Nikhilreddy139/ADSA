#904 Problem: Fruit Into Baskets
from typing import List
def totalFruit(fruits: List[int]) -> int:
    count = {}
    left = 0
    max_picked = 0
    for right in range(len(fruits)):
        count[fruits[right]] = count.get(fruits[right], 0) + 1            
        while len(count) > 2:
            count[fruits[left]] -= 1
            if count[fruits[left]] == 0:
                del count[fruits[left]]
            left += 1            
        max_picked = max(max_picked, right - left + 1)
    return max_picked
fruits = [1,2,1]
print(totalFruit(fruits))
print()

#3 Problem: Longest Substring Without Repeating Characters
from typing import List
def lengthOfLongestSubstring(s: str) -> int:
    seen = set()
    l,ans=0,0
    for r in range(len(s)):
        while s[r] in seen:
            seen.remove(s[l])
            l+=1
        seen.add(s[r])
        ans = max(ans,r-l+1)
    return ans
s = "abcabcbb"
print(lengthOfLongestSubstring(s))