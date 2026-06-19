class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tempStack = []
        res = [0 for i in range(len(temperatures))]

        for i, t in enumerate(temperatures):
            while tempStack and t > tempStack[-1][0]:
                stackT, stackI = tempStack.pop() 
                res[stackI] = i - stackI
            tempStack.append((t, i))

        return res

