class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        highest = 0
        for i in range(len(heights)):
            minimum = heights[i]    
            for j in range(i, len(heights)):
                minimum = min(minimum, heights[j])
                rectangle = minimum * ((j+1)-i)
                highest = max(rectangle, highest)

        return highest
        

            