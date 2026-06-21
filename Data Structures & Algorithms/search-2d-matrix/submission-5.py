class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix)-1
        row = []
        while top <= bottom:
            midrow = (top+bottom) // 2
            if matrix[midrow][0] > target:
                bottom = midrow - 1
            elif matrix[midrow][-1] < target:
                top = midrow + 1
            else:
                row = matrix[midrow]
                break

        if not row:
            return False

        l, r = 0, len(row)-1
        while l <= r:
            m = (l+r) // 2
            print(l, r, m)
            if row[m] > target:
                r = m - 1
            elif row[m] < target:
                l = m + 1
            else:
                return True
        return False