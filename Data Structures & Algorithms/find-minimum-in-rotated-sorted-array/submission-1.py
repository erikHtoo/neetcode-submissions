class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r) // 2
            print(nums[l], nums[m], nums[r])
            if nums[m] > nums[l] and nums[m] > nums[r]:
                l = m 
            elif nums[m] < nums[r]:
                r = m 
            else:
                return min(nums[l], nums[r])