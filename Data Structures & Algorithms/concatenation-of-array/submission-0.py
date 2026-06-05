class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # loop thru the array twice
            # add char to ans
        ans = []
        for n in range(2):
            for num in nums:
               ans.append(num)
        return ans 