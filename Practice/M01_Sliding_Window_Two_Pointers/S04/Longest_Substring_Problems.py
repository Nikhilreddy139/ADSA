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