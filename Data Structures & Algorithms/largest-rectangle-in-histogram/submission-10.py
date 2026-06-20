class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                start, popped_height = stack.pop()
                maxArea = max((i-start)*popped_height, maxArea)

            stack.append((start, h))
            
        length = len(heights)
        while stack:
            i, h = stack.pop()
            maxArea = max((length-i)*h, maxArea)

        return maxArea
        

            