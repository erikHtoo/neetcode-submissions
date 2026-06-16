class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        print(digits)
        res = 0
        for i in range(len(digits)):
            res += digits[i] * (10**i)
        res += 1
        ans = []
        for n in str(res):
            ans.append(int(n))
        return ans