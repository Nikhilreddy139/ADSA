def Check_Palindrome(n: int, s: str) -> bool:
    left = 0
    right = n - 1
    while left < right:
        if s[left] != s[right]:
            left_delete = s[left + 1:right + 1]
            right_delete = s[left:right]
            return left_delete == left_delete[::-1] or right_delete == right_delete[::-1]
        left += 1
        right -= 1
    return True
if __name__ == '__main__':
    n = int(input())
    s = input()
    print(Check_Palindrome(n, s))