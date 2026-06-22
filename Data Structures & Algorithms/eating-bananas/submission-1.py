class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            m = (l+r) // 2
            time = 0
            for p in piles:
                time += math.ceil(p/m)
            print("time taken: ", time)
            print("with eating rate of: ", m)
            if time <= h:
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1

        return res