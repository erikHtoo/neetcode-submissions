class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = ""
        for c in s:
            if c.isalnum():
                newstr += c
        left = 0
        right = len(newstr)-1
        while left < right:
            print(newstr[left], left, newstr[right], right)
            if newstr[left].lower() != newstr[right].lower():
                return False
            left += 1
            right -= 1
        return True
